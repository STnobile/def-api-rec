from django.db.models import Sum
from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    owner_id = serializers.ReadOnlyField(source="owner.id")

    class Meta:
        model = Booking
        fields = [
            "id",
            "owner",
            "owner_id",
            "date",
            "tour_section",
            "time_slot",
            "max_capacity",
            "num_of_people",
            "current_capacity",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "owner",
            "owner_id",
            "max_capacity",
            "current_capacity",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        date = attrs.get("date", getattr(self.instance, "date", None))
        time_slot = attrs.get(
            "time_slot", getattr(self.instance, "time_slot", None)
        )
        tour_section = attrs.get(
            "tour_section", getattr(self.instance, "tour_section", None)
        )
        num_of_people = attrs.get(
            "num_of_people", getattr(self.instance, "num_of_people", None)
        )

        if None in (date, time_slot, tour_section, num_of_people):
            return attrs

        max_capacity = (
            self.instance.max_capacity
            if self.instance
            else Booking().max_capacity
        )

        existing_bookings = Booking.objects.filter(
            date=date,
            time_slot=time_slot,
            tour_section=tour_section,
        )
        if self.instance:
            existing_bookings = existing_bookings.exclude(id=self.instance.id)

        existing_capacity = (
            existing_bookings.aggregate(Sum("num_of_people"))[
                "num_of_people__sum"
            ]
            or 0
        )
        if existing_capacity + num_of_people > max_capacity:
            raise serializers.ValidationError(
                {
                    "num_of_people": (
                        "Maximum capacity reached for this time slot "
                        "in the selected section."
                    )
                }
            )

        return attrs

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
