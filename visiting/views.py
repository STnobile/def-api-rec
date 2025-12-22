from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer
from .permissions import IsOwnerOrReadOnly

class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(owner=self.request.user).order_by('date', 'time_slot', 'tour_section')

    def perform_create(self, serializer):
        booking = serializer.save(owner=self.request.user)
        booking.update_current_capacity()
class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
