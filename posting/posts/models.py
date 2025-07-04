from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author    = models.ForeignKey(User, on_delete=models.CASCADE)
    title     = models.CharField(max_length=200)
    image     = models.ImageField(upload_to='post_images/', blank=True, null=True)
    content   = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title