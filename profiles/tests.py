from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Profile

class ProfileListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        User.objects.all().delete()  # Clear all users before the test
        Profile.objects.all().delete()  # Clear all profiles before the test
        self.user1 = User.objects.create_user(username='user1', password='testpassword')
        self.user2 = User.objects.create_user(username='user2', password='testpassword')
        

    def test_list_profiles(self):
        url = reverse('profiles-list')  # Adjust this to match your actual URL name
        response = self.client.get(url)
        print("Response data:", response.data)  # This will print the response data in your test output
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2, msg=f"Expected 2 profiles, found {len(response.data['results'])}: {response.data}")


