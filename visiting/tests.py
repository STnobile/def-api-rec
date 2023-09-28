from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Booking

class BookingTests(APITestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        
        # Sample booking data
        self.booking_data = {
            'post': 'Test booking',
            'date': '2023-10-10',
            'time_slot': '10:00 am - 11:30 am',
            'num_of_people': 2
        }

    def test_create_booking(self):
        response = self.client.post('/visiting/', self.booking_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.get().num_of_people, 2)

    def test_update_booking(self):
        response = self.client.post('/visiting/', self.booking_data, format='json')
        booking = Booking.objects.get()

        updated_data = {
            'post': 'Updated booking',
            'date': '2023-10-11',
            'time_slot': '12:00 pm - 1:30 pm',
            'num_of_people': 3
        }
        response = self.client.put(f'/visiting/{booking.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        booking.refresh_from_db()
        self.assertEqual(booking.num_of_people, 3)

    def test_delete_booking(self):
        response = self.client.post('/visiting/', self.booking_data, format='json')
        booking = Booking.objects.get()
        response = self.client.delete(f'/visiting/{booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)

    def test_exceed_capacity(self):
        # Assuming the max capacity is 28, and each booking is for 14 people
        # Two bookings should be allowed, but the third should fail
        self.booking_data['num_of_people'] = 14
        response1 = self.client.post('/visiting/', self.booking_data, format='json')
        response2 = self.client.post('/visiting/', self.booking_data, format='json')
        response3 = self.client.post('/visiting/', self.booking_data, format='json')

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response3.status_code, status.HTTP_400_BAD_REQUEST)


