from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404 
from .serializers import CustomTokenObtainPairSerializer, UserSerializer, PostSerializer, CommentSerializer, ReplySerializer
from .models import Post, Comment, Reply

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post_id = self.request.data.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(user=self.request.user, post=post)

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReplyListCreateView(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        comment_id = self.request.data.get('comment_id')
        comment = get_object_or_404(Comment, pk=comment_id)
        serializer.save(user=self.request.user, comment=comment)

class ReplyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]