from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.db.models import Sum
from .models import Booking
from .serializers import BookingSerializer
from .permissions import IsOwnerOrReadOnly

class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Booking.objects.filter(owner=self.request.user).order_by('date', 'time_slot')

    def create(self, request, *args, **kwargs):
        # Extract data from the request
        date = request.data['date']
        time_slot = request.data['time_slot']
        num_of_people = int(request.data['num_of_people'])  # Convert num_of_people to an integer

        # Check if the current_capacity exceeds the max_capacity (28)
        existing_capacity = Booking.objects.filter(date=date, time_slot=time_slot).aggregate(Sum('num_of_people'))['num_of_people__sum']
        if existing_capacity is not None and existing_capacity + num_of_people > 28:
            return Response({'error': 'Maximum capacity reached for this time slot.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new booking and set the owner
        new_booking = Booking.objects.create(
            owner=request.user,
            date=date,
            time_slot=time_slot,
            num_of_people=num_of_people
        )

        # Update the current_capacity based on existing bookings
        new_booking.update_current_capacity()

        # Serialize the created booking
        serializer = self.get_serializer(new_booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Ensure to not directly decrement current_capacity. 
        # Instead, calculate it again based on remaining bookings 
        # or use the @property method.
        instance.update_current_capacity()

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

