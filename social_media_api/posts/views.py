from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment, Like
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from notifications.models import Notification
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import generics

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get posts from users the current user is following
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    user = request.user

    # Check if user has already liked the post
    if Like.objects.filter(user=user, post=post).exists():
        return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    # Create a like
    like = Like.objects.get_or_create(user=request.user, post=post)
    
    # Create notification
    Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb='liked',
        target=post
    )
    
    return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    # Check if the user has liked the post
    like = Like.objects.filter(user=user, post=post).first()
    if not like:
        return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    # Unlike the post
    like.delete()

    return Response({'detail': 'Post unliked successfully.'}, status=status.HTTP_204_NO_CONTENT)

