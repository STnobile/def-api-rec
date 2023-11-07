from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Booking

class BookingViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.booking = Booking.objects.create(
            owner=self.user,
            date='2023-11-07',
            time_slot='10:00 am - 11:30 am',
            tour_section='Museum',
            num_of_people=2
        )

    def test_create_booking(self):
        url = reverse('visiting-list-create')
        data = {
            'date': '2023-11-07',
            'time_slot': '10:00 am - 11:30 am',
            'tour_section': 'Museum',
            'num_of_people': 2,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)  # Assuming another booking was added

    def test_get_booking_list(self):
       url = reverse('visiting-list-create')
       response = self.client.get(url, format='json')
       print(response.data)  # Add this line to print the response data
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       self.assertEqual(len(response.data['results']), 1)

    def test_get_booking_detail(self):
        url = reverse('visiting-detail', kwargs={'pk': self.booking.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['num_of_people'], 2)

    def test_update_booking(self):
        url = reverse('visiting-detail', kwargs={'pk': self.booking.pk})
        data = {
            'num_of_people': 3,
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.num_of_people, 3)

    def test_delete_booking(self):
        url = reverse('visiting-detail', kwargs={'pk': self.booking.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)