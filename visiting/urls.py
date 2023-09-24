from django.urls import path
from .views import BookingListCreateView, BookingDetailView

urlpatterns = [
    path('visiting/', BookingListCreateView.as_view(), name='visiting-list-create'),
    path('visiting/<int:pk>/', BookingDetailView.as_view(), name='visiting-detail'),
]