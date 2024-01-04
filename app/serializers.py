from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Reply

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name','last_name','username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ReplySerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Reply
        fields = ['id', 'text', 'username', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    replies = ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'username', 'replies', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    username = serializers.ReadOnlyField(source='user.username')  

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'image', 'likes', 'username', 'comments', 'created_at']