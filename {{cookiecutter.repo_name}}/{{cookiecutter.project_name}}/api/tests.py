from rest_framework import status
from rest_framework.test import APITestCase


class SampleTestCase(APITestCase):
    def test_url_root(self):
        url = '/api/'
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))
