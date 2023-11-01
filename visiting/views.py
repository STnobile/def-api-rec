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
        return Booking.objects.filter(owner=self.request.user).order_by('date', 'time_slot', 'section')

    def create(self, request, *args, **kwargs):
        date = request.data['date']
        time_slot = request.data['time_slot']
        section = request.data['section']
        num_of_people = int(request.data['num_of_people'])

        existing_capacity = Booking.objects.filter(date=date, time_slot=time_slot, section=section).aggregate(Sum('num_of_people'))['num_of_people__sum'] or 0
        if existing_capacity + num_of_people > 28:
            return Response({'error': 'Maximum capacity reached for this time slot in the selected section.'}, status=status.HTTP_400_BAD_REQUEST)

        new_booking = Booking.objects.create(
            owner=request.user,
            date=date,
            time_slot=time_slot,
            section=section,
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # If you're recalculating and updating some current_capacity field,
        # you might want to perform the update after the booking deletion.
        self.perform_destroy(instance)

        instance.update_current_capacity()

        return Response(status=status.HTTP_204_NO_CONTENT)
