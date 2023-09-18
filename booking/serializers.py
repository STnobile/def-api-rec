from rest_framework import serializers
from .models import Visit
from django.utils import timezone

class VisitSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S%z", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S%z", read_only=True)

    def get_is_owner(self, obj):
        request = self.context.get('request')
        if request:
            return request.user == obj.owner
        return False
    
    class Meta:
        model = Visit
        fields = [
            'id', 'owner_username', 'is_owner', 'profile_id',
            'created_at', 'updated_at',
            'location', 'date', 'time', 'is_confirmed',
        ]