from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.text

class Reply(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text