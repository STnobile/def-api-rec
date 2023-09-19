from django.urls import path
from .views import BookingListCreateView, BookingRetrieveUpdateDestroyView, TimeSlotListCreateView

urlpatterns = [
    path('bookings/', BookingListCreateView.as_view()),
    path('bookings/<int:pk>/', BookingRetrieveUpdateDestroyView.as_view()),
]
