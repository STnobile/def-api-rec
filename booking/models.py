from django.db import models

class TimeSlot(models.Model):
    SLOT_CHOICES = [
        ("10:00", "10:00 AM - 11:30 AM"),
        ("12:00", "12:00 PM - 1:30 PM"),
        ("16:00", "4:00 PM - 5:30 PM"),
        ("18:00", "6:00 PM - 7:30 PM"),
    ]

    slot_start = models.TimeField(choices=SLOT_CHOICES, default='10:00')

    def __str__(self):
        return f"{self.get_slot_start_display()}"

class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
