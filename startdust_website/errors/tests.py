from django.test import TestCase
from errors.models import Error


class ErrorModelTestCase(TestCase):

    def test_error_model_should_have_a_date_attribute(self):
        '''
        error model should have a date attribue
        '''
        for field in Error._meta.fields:
            if field.name == 'date':
                return

        assert False

    def test_error_model_should_have_a_url_attribute(self):
        '''
        error model should have a url attribute
        '''
        for field in Error._meta.fields:
            if field.name == 'url':
                return

        assert False

    def test_error_model_should_have_a_traceback_attribute(self):
        '''
        error model should have a traceback attribute
        '''
        for field in Error._meta.fields:
            if field.name == 'traceback':
                return

        assert False

    def test_error_model_should_have_a_exception_attribute(self):
        '''
        error model should have a exception attribute
        '''
        for field in Error._meta.fields:
            if field.name == 'exception':
                return

        assert False
