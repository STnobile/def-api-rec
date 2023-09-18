from django.urls import path
from .views import VisitListCreateView, VisitRetrieveUpdateDestroyView

urlpatterns = [
    path('visits/', VisitListCreateView.as_view()),
    path('visits/<int:pk>/', VisitRetrieveUpdateDestroyView.as_view()),
    ]