from django.db import IntegrityError
from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id', 'owner', 'created_at', 'post'
            # Add any other fields from the Like model that you want to include in the response
        ]

    def create(self, validate_data):
        try:
            return super().create(validate_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail' : 'possible duplicate'
            })    