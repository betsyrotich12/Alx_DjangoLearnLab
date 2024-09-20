from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import FollowUserSerializer, RegisterSerializer, LoginSerializer, ProfileSerializer, UnfollowUserSerializer

User = get_user_model()

# Registration view
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = Token.objects.create(user=user)
        response_data = {
            'token': token.key,
            'username': user.username,
            'email': user.email
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

# Login view
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

# Profile view (retrieves the logged-in user's profile)
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)
        if request.user.is_following(user_to_follow):
            return Response({'detail': 'You are already following this user.'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.follow(user_to_follow)
        serializer = FollowUserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)
        if not request.user.is_following(user_to_unfollow):
            return Response({'detail': 'You are not following this user.'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.unfollow(user_to_unfollow)
        serializer = UnfollowUserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

