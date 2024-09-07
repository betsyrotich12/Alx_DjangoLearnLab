from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class BookListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class BookDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class BookCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
         if 'author' not in request.data:
            return Response({"error": "Author is required."}, status=400)
         return self.create(request, *args, **kwargs)
    
class BookUpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()

    def put(self, request, *args, **kwargs):
         book_instance = self.get_object()
         if book_instance.publication_year > 2024:
            return Response({"error": "Publication year cannot be in the future."}, status=400)
         return self.update(request, *args, **kwargs)
    
class BookDeleteView(mixins.DestroyModelMixin, generics.GenericAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer
     permission_classes = [IsAuthenticatedOrReadOnly]

     def delete(self, request, *args, **kwargs):
         return self.destroy( request, *args, **kwargs)




