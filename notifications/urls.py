from django.urls import path
from .views import NotificationListView, NotificationUpdateView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', NotificationUpdateView.as_view(), name='notification-detail'),
]