from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def create(self, validated_data):
        # The 'super().create(validated_data)' call creates a new Booking instance
        # from the validated data.
        booking = super().create(validated_data)
        
        booking.update_current_capacity()
        
        return booking

    def update(self, instance, validated_data):
        # The 'super().update(instance, validated_data)' call updates the instance
        # with the validated data.
        instance = super().update(instance, validated_data)
        
        # Again, we call 'update_current_capacity' to update the capacity.
        instance.update_current_capacity()
        
        return instance
