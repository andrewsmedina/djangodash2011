from django.test import TestCase
from datetime import datetime
from errors.models import Error
from errors.forms import ErrorForm


class ErrorFormTestCase(TestCase):

    def test_error_form_should_use_error_model(self):
        '''
        ErrorForm should use Error model for form generation
        '''
        self.assertEqual(Error, ErrorForm._meta.model)


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

    def test_error_model_should_have_a_project_related(self):
        '''
        error should related with project
        '''
        self.assertFieldIn('project', Error._meta.fields)

    def test_unicode_for_error_should_return_error_exception(self):
        '''
        error unicode should returns error exception
        '''
        error = Error.objects.create(
            date=datetime.now(),
            exception='exception',
            traceback='traceback',
            url='http://error/url'
        )

        self.assertEqual(error.exception, unicode(error))

    def assertFieldIn(self, expected_field, field_list):
        '''
        assert if field in a field list
        '''
        self.assertTrue(expected_field in [field.name for field in field_list])
