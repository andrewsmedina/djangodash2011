from django.test import TestCase
from responses.models import Response


class ResponseModelTestCase(TestCase):

    def test_response_model_should_have_time_attribute(self):
        '''
        Response model should have time attribute
        '''
        self.assertFieldIn('time', Response._meta.fields)

    def test_response_model_should_have_url_attribute(self):
        '''
        Response model should have url attribute
        '''
        self.assertFieldIn('url', Response._meta.fields)

    def assertFieldIn(self, expected_field, field_list):
        '''
        assert if field in a field list
        '''
        self.assertTrue(expected_field in [field.name for field in field_list])
