from django.db import models
from datetime import datetime
from django.db.models import Sum
from django.contrib.auth.models import User

class Booking(models.Model):
    date = models.DateField()
    time_slot = models.CharField(max_length=30, choices=[
        ('10:00 am - 11:30 am', '10:00 am - 11:30 am'),
        ('12:00 pm - 1:30 pm', '12:00 pm - 1:30 pm'),
        ('4:00 pm - 5:30 pm', '4:00 pm - 5:30 pm'),
        ('6:00 pm - 7:30 pm', '6:00 pm - 7:30 pm'),
    ])
    max_capacity = models.PositiveIntegerField(default=28)
    num_of_people = models.PositiveIntegerField(default=1)
    current_capacity = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return f"Booking on {self.date} at {self.time_slot}"

    
    def update_current_capacity(self):
        total_num_of_people = Booking.objects.filter(date=self.date, time_slot=self.time_slot).aggregate(Sum('num_of_people'))['num_of_people__sum']
        if total_num_of_people is not None:
            self.current_capacity = total_num_of_people
        else:
            self.current_capacity = 0
        self.save()

