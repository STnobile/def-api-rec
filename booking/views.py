from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all().order_by('date', 'time_slot')
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        time_slot = request.data['time_slot']
        current_capacity = Booking.objects.filter(time_slot=time_slot).count()

        if current_capacity >= 17:  # Check if current capacity is equal to or greater than the maximum
            return Response({'error': 'Maximum capacity reached for this time slot.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new booking
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Update the booked count
        booking = Booking.objects.get(pk=serializer.data['id'])
        booking.booked_count = current_capacity + 1  # Increment current capacity
        booking.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.booked_count > 0:
            instance.booked_count -= 1  # Decrement booked count
            instance.save()

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
