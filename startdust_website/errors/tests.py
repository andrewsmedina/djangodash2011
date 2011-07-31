from django.test import TestCase
from datetime import datetime
from errors.models import Error
from errors.forms import ErrorForm
from projects.models import Project


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

    def test_response_should_be_ordered_by_date_desc(self):
        '''
        Response should be ordered by -date
        '''
        self.assertIn('-date', Error._meta.ordering)

    def test_get_absolute_url_should_return_url_of_error(self):
        '''
        url should be /panel/projects/1/error/1/
        '''
        project = Project.objects.create(name='testee', url=u'http://aaaa.com', token='111111')
        error = Error.objects.create(
            date=datetime.now(),
            exception='exception',
            traceback='traceback',
            url='http://error/url',
            project=project
        )
        self.assertEqual(error.get_absolute_url(), '/panel/projects/%s/error/%s/' % (project.id, error.id))

    def assertFieldIn(self, expected_field, field_list):
        '''
        assert if field in a field list
        '''
        self.assertTrue(expected_field in [field.name for field in field_list])
