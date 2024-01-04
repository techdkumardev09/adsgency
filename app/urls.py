from django.urls import path
from .views import (
    RegisterUserView,
    ObtainTokenPairView,
    PostListCreateView,
    PostRetrieveUpdateDestroyView,
    CommentListCreateView,
    CommentRetrieveUpdateDestroyView,
    ReplyListCreateView,
    ReplyRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("token/", ObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-retrieve-update-destroy'),
    path('replies/', ReplyListCreateView.as_view(), name='reply-list-create'),
    path('replies/<int:pk>/', ReplyRetrieveUpdateDestroyView.as_view(), name='reply-retrieve-update-destroy'),
]
