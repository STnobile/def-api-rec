from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from django.db.models import Sum


class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all().order_by('date', 'time_slot')
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        time_slot = request.data.get('time_slot')
        # Default to 1 if not provided
        num_people = int(request.data.get('num_people', 1))
        current_capacity = Booking.objects.filter(time_slot=time_slot).aggregate(
            Sum('num_people'))['num_people__sum'] or 0

        if current_capacity + num_people > 17:
            return Response({'error': 'Booking exceeds maximum capacity for this time slot.'}, status=status.HTTP_400_BAD_REQUEST)

         # Create a new booking
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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
