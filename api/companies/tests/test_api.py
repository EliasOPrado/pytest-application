import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
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
            # 'last_update': '2021-04-20T20:58:12Z',
            'notes': 'dumb note'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(Company.objects.get().name, 'IBM')


    def test_get_company(self):
        """GET method."""
        url = reverse('companies:companies-list')

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_update_company(self):
    #     """
    #     UPDATE method.
    #     """
    #     url = reverse('companies:companies-detail', kwargs={'pk': 1})

    #     data = {verse('companies:companies-detail', kwargs={'pk': 1})

    #     data = {
    #         'id': 1,
    #         'name': 'IBM2',
    #         'status': 'Hiring',
    #         'application_link': 'https://dumb.domains/',
    #         'last_update': '2021-04-20T20:58:12Z',
    #         'notes': 'dumb note'
    #     }
    
    #     response = self.client.put(url, data)
    #     print(response.content)
    #     self.assertEqual(json.loads(response.content), data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Company.objects.get().name, 'IBM2')
