import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from companies.models import Company



class CompanyTestCase(APITestCase):
    def test_create_company(self):
        """
        POST method
        """

        url = reverse('companies:companies-list')

        data = {
            'name': 'IBM',
            'status': 'Hiring',
            'application_link': 'https://dumb.domains/',
            'last_update': '2021-04-20T20:58:12Z',
            'notes': 'dumb note'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(Company.objects.get().name, 'IBM')


    def test_get_company(self):
        """GET method."""
        
        url = reverse('companies:companies-list')

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_company(self):
        """
          UPDATE method.
        """

        company_list = Company.objects.create(name='samplemed', 
        status='Hiring', application_link='', last_update='2021-04-20T20:58:12Z',
        notes='')
        print("TEST HERE +++>", company_list)
        url = reverse('companies:companies-detail', kwargs={'pk': company_list.pk})

        data = {
            'id':company_list.pk,
            'name': 'Portoseguro',
            'status': 'Hiring',
            'application_link': 'https://dumb.domains/',
            'last_update': '2021-04-20T20:58:12Z',
            'notes': 'dumb note'
        }

        response = self.client.put(url, data)
        print(response.content)
        self.assertEqual(json.loads(response.content), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
