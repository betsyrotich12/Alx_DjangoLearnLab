from django.urls import path
from .views import CommentCreateView, CommentDeleteView, CommentUpdateView, CustomLoginView, CustomLogoutView, RegisterView, profile_view
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='create_comment'),
    path('post/<int:post_id>/comments/<int:comment_id>/update/', CommentUpdateView.as_view(), name='update_comment'),
    path('post/<int:post_id>/comments/<int:comment_id>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]

