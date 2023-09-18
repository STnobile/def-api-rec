from django.db import models
from django.contrib.auth.models import User

class Visit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.owner.username} - {self.location} - {self.date} {self.time}"