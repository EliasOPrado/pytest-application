
from django.test import TestCase
from companies.models import Company
from django.utils import timezone
import datetime

class TestModels(TestCase):

    def test_destinations_model(self):
        #test if Destinations model is passing correctly its values
        company = Company.objects.create(
            name = 'Samplemed',
            status ='Hiring Freeze',
            last_update = '2021-04-20T20:58:12Z',
            application_link = 'https://dumb.domains/',
            notes ='test note',
        )
        company.save()
        self.assertEquals(company.name, 'Samplemed')
        self.assertEquals(company.status, 'Hiring Freeze')
        self.assertEquals(company.last_update, '2021-04-20T20:58:12Z')
        self.assertEquals(company.application_link, 'https://dumb.domains/')
        self.assertEquals(company.notes, 'test note')