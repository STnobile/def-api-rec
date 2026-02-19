from django.db.models import Count, OuterRef, Subquery
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer
from likes.models import Like


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Post.objects.annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('comment', distinct=True),
        ).select_related('owner', 'owner__profile').order_by('-created_at')
        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.annotate(
                like_id=Subquery(
                    Like.objects.filter(owner=user, post=OuterRef('pk'))
                    .values('id')[:1]
                )
            )
        return queryset

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        # user feed
        'owner__followed__owner__profile',
        # user likes posts
        'likes__owner__profile',
        # user posts
        'owner__profile',
    ]

    search_fields = [
        'owner__username',
        'title',
    ]
    
    ordering_fields = [ 
        'created_at', 
        'comments_count', 
        'likes_count'
    ]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def get_queryset(self):
        queryset = Post.objects.annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('comment', distinct=True),
        ).select_related('owner', 'owner__profile').order_by('-created_at')
        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.annotate(
                like_id=Subquery(
                    Like.objects.filter(owner=user, post=OuterRef('pk'))
                    .values('id')[:1]
                )
            )
        return queryset
