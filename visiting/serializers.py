from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def create(self, validated_data):
        booking = super().create(validated_data)
        
        # Update the current capacity when creating a booking
        booking.update_current_capacity()
        
        return booking

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        
        # Update the current capacity when updating a booking
        instance.update_current_capacity()
        
        return instance