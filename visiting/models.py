from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

class Booking(models.Model):
    owner = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
     
    # Fields for booking
    date = models.DateField()


    TOUR_SECTIONS = [
        ('Museum', 'Museum'),
        ('Photos Gallery', 'Photos Gallery'),
        ('Underground Wine tanks', 'Under Ground Wine tanks'),
        ('Private Garden', 'Private Garden'),
    ]
    section = models.CharField(max_length=100, choices=TOUR_SECTIONS, default='Choose here!')

    # Changed time_slot to CharField
    time_slot = models.CharField(
        max_length=50,
        choices=[
            ('10:00 am - 11:30 am', '10:00 am - 11:30 am'),
            ('12:00 pm - 1:30 pm', '12:00 pm - 1:30 pm'),
            ('4:00 pm - 5:30 pm', '4:00 pm - 5:30 pm'),
            ('6:00 pm - 7:30 pm', '6:00 pm - 7:30 pm'),
        ]
    )
    
    
    max_capacity = models.PositiveIntegerField(default=28)
    num_of_people = models.PositiveIntegerField(default=1)
    current_capacity = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking by {self.owner.username} for {self.section} on {self.date} at {self.time_slot}"

    def get_current_capacity(self):
        total_num_of_people = Booking.objects.filter(
            date=self.date, time_slot=self.time_slot, section=self.section
        ).aggregate(total=Sum('num_of_people'))['total'] or 0
        return total_num_of_people

    def update_current_capacity(self):
        # Note the change here: We're using the method instead of the property
        self.current_capacity = self.get_current_capacity()
        self.save()