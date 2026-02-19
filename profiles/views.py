from django.db.models import Count, OuterRef, Subquery
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer
from followers.models import Follower



class ProfileList(generics.ListAPIView):
    """
    List all profiles
    No Create view (post method), as profile creation handled by django signals
    """
    def get_queryset(self):
        queryset = Profile.objects.annotate(
            posts_count=Count('owner__post', distinct=True),
            followers_count=Count('owner__followed', distinct=True),
            following_count=Count('owner__following', distinct=True),
        ).select_related('owner').order_by('-created_at')
        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.annotate(
                following_id=Subquery(
                    Follower.objects.filter(owner=user, followed=OuterRef('owner'))
                    .values('id')[:1]
                )
            )
        return queryset
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at'
    ]

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    def get_queryset(self):
        queryset = Profile.objects.annotate(
            posts_count=Count('owner__post', distinct=True),
            followers_count=Count('owner__followed', distinct=True),
            following_count=Count('owner__following', distinct=True),
        ).select_related('owner').order_by('-created_at')
        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.annotate(
                following_id=Subquery(
                    Follower.objects.filter(owner=user, followed=OuterRef('owner'))
                    .values('id')[:1]
                )
            )
        return queryset
    serializer_class = ProfileSerializer
