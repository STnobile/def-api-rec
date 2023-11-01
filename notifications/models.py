from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    TYPE_CHOICES = [
        ('POST', 'Post Created'),
        ('COMMENT', 'Comment Made'),
        ('LIKE', 'Like'),
        ('FOLLOW', 'New Follower'),
    ]
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    content = models.TextField()
    reference_id = models.IntegerField()  
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

