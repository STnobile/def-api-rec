from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=30, choices=[
        ('10:00 am - 11:30 am', '10:00 am - 11:30 am'),
        ('12:00 pm - 1:30 pm', '12:00 pm - 1:30 pm'),
        ('4:00 pm - 5:30 pm', '4:00 pm - 5:30 pm'),
        ('6:00 pm - 7:30 pm', '6:00 pm - 7:30 pm'),
    ])
    num_people = models.PositiveIntegerField(default=1)
    max_capacity = 17
    current_capacity = models.PositiveIntegerField(default=0)
    booked_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Booking on {self.date} at {self.time_slot}"







