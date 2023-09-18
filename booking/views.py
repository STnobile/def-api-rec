from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Visit
from .serializers import VisitSerializer

class VisitListCreateView(generics.ListCreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated]  # Require authentication for booking

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Associate the booking with the current user

class VisitRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated]  # Require authentication for editing or deleting a booking

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)  # Make sure the user who booked can edit it





