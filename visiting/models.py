from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

class Booking(models.Model):
    owner = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    
    # Post can be a comment or description about the booking
    post = models.TextField(blank=True, null=True) 
    
    # Fields for booking
    date = models.DateField()
    time_slot = models.PositiveSmallIntegerField(
        choices=[
            (1, '10:00 am - 11:30 am'),
            (2, '12:00 pm - 1:30 pm'),
            (3, '4:00 pm - 5:30 pm'),
            (4, '6:00 pm - 7:30 pm'),
        ]
    )
    max_capacity = models.PositiveIntegerField(default=28)
    num_of_people = models.PositiveIntegerField(default=1)
    current_capacity = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking by {self.owner.username} on {self.date} at {self.get_time_slot_display()}"

    def get_current_capacity(self):
        total_num_of_people = Booking.objects.filter(
            date=self.date, time_slot=self.time_slot
        ).aggregate(total=Sum('num_of_people'))['total'] or 0
        return total_num_of_people

    def update_current_capacity(self):
        # Note the change here: We're using the method instead of the property
        self.current_capacity = self.get_current_capacity()
        self.save()