from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def create(self, validated_data):
        # Update the current capacity when creating a booking
        booking = Booking.objects.create(**validated_data)
        booking.current_capacity += 1
        booking.save()
        return booking

    def update(self, instance, validated_data):
        # Update the current capacity when updating a booking
        instance.date = validated_data.get('date', instance.date)
        instance.time_slot = validated_data.get('time_slot', instance.time_slot)
        instance.max_capacity = validated_data.get('max_capacity', instance.max_capacity)
        instance.current_capacity = validated_data.get('current_capacity', instance.current_capacity)
        instance.save()
        return instance
