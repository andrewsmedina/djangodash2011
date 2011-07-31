from django.test import TestCase
from requests.models import Request


class RequestModelTestCase(TestCase):

    def test_request_model_should_have_url_attribute(self):
        '''
        Request model should have url attribute
        '''
        self.assertFieldIn('url', Request._meta.fields)

    def test_request_model_should_have_date_attribute(self):
        '''
        Request model should have date attribute
        '''
        self.assertFieldIn('date', Request._meta.fields)

    def test_request_model_should_be_related_with_project(self):
        '''
        Request model shoudl be related with Project model
        '''
        self.assertFieldIn('project', Request._meta.fields)

    def assertFieldIn(self, expected_field, field_list):
        '''
        assert if field in a field list
        '''
        self.assertTrue(expected_field in [field.name for field in field_list])
