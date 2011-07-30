from django.test import TestCase
from errors.models import Error


class ErrorModelTestCase(TestCase):

    def test_error_model_should_have_a_date_attribute(self):
        '''
        error model should have a date attribue
        '''
        self.assertFieldIn('date', Error._meta.fields)

    def test_error_model_should_have_a_url_attribute(self):
        '''
        error model should have a url attribute
        '''
        self.assertFieldIn('url', Error._meta.fields)

    def test_error_model_should_have_a_traceback_attribute(self):
        '''
        error model should have a traceback attribute
        '''
        self.assertFieldIn('traceback', Error._meta.fields)

    def test_error_model_should_have_a_exception_attribute(self):
        '''
        error model should have a exception attribute
        '''
        self.assertFieldIn('exception', Error._meta.fields)

    def assertFieldIn(self, expected_field, field_list):
        '''
        assert if field in a field list
        '''
        self.assertTrue(expected_field in [field.name for field in field_list])
