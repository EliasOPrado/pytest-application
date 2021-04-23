from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.companies.models import Company


class CompanyTestCase(APITestCase):
    def test_create_company(self):
        """ POST ====
        Ensure we can create a new company object.
        """
        url = reverse('/')
        data = {
            'name': 'IBM',
            'status': 'Hiring',
            'application_link': 'https://dumb.domains/',
            #'last_update': '2021-04-20T20:58:12Z',
            'notes': 'dumb note'
        }
        response = self.client.post(url, data, format='json')
        print("HEERER", response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(Company.objects.get().name, 'IBM')