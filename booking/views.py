from rest_framework import generics, permissions
from rest_framework import status
from .models import Booking
from rest_framework.response import Response 
from .serializers import BookingSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        # Check if the maximum capacity is reached
        if Booking.objects.filter(date=request.data['date'], time_slot=request.data['time_slot']).count() >= 17:
            return Response({'error': 'Maximum capacity reached for this time slot.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new booking
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Update the current capacity
        booking = Booking.objects.get(pk=serializer.data['id'])
        booking.current_capacity += 1
        booking.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Update the current capacity when a booking is deleted
        instance.current_capacity -= 1
        instance.save()

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)