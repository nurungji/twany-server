from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.core.urlresolvers import reverse


# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.member_data = {'name': 'Nick'}
        self.response = self.client.post(
            reverse('create'),
            self.member_data,
            format="json")

    def test_api_can_create_a_member(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)