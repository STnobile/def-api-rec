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
        return Booking.objects.filter(owner=self.request.user).order_by('date', 'time_slot', 'tour_section')


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        num_of_people = serializer.validated_data['num_of_people']
        existing_capacity = Booking.objects.filter(
            date=serializer.validated_data['date'],
            time_slot=serializer.validated_data['time_slot'],
            tour_section=serializer.validated_data['tour_section']
        ).aggregate(Sum('num_of_people'))['num_of_people__sum'] or 0

        if existing_capacity + num_of_people > 28:
            return Response({'error': 'Maximum capacity reached for this time slot in the selected section.'}, status=status.HTTP_400_BAD_REQUEST)

        new_booking = serializer.save(owner=request.user)
        new_booking.update_current_capacity()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

        existing_capacity = Booking.objects.filter(date=date, time_slot=time_slot, tour_section=tour_section).aggregate(
            Sum('num_of_people'))['num_of_people__sum'] or 0
        if existing_capacity + num_of_people > 28:
            return Response({'error': 'Maximum capacity reached for this time slot in the selected section.'}, status=status.HTTP_400_BAD_REQUEST)

        new_booking = Booking.objects.create(
            owner=request.user,
            date=date,
            time_slot=time_slot,
            tour_section=tour_section,
            num_of_people=num_of_people
        )

        # Assuming update_current_capacity updates a certain capacity field in Booking.
        new_booking.update_current_capacity()

        serializer = self.get_serializer(new_booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def update(self, request, *args, **kwargs):
        booking_instance = self.get_object()
        date = request.data.get('date', booking_instance.date)
        time_slot = request.data.get('time_slot', booking_instance.time_slot)
        tour_section = request.data.get(
            'tour_section', booking_instance.tour_section)
        num_of_people = int(request.data.get(
            'num_of_people', booking_instance.num_of_people))

        # Check if the updated booking would exceed capacity
        existing_bookings = Booking.objects.filter(
            date=date,
            time_slot=time_slot,
            tour_section=tour_section
        ).exclude(id=booking_instance.id)  # Exclude the current booking from the capacity check

        existing_capacity = existing_bookings.aggregate(
            Sum('num_of_people'))['num_of_people__sum'] or 0
        if existing_capacity + num_of_people > 28:
            raise ValidationError(
                {'error': 'Maximum capacity reached for this time slot in the selected section.'})

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Call update_current_capacity before destroying the instance
        instance.update_current_capacity()
        self.perform_destroy(instance)
        # Do not call any method on the instance after it has been deleted
        return Response(status=status.HTTP_204_NO_CONTENT)
