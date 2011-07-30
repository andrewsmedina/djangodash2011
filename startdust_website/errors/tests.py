from django.test import TestCase
from errors.models import Error


class ErrorModelTestCase(TestCase):

    def test_error_should_have_a_date_attribute(self):
        '''
        error model should have a date attribue
        '''
        for field in Error._meta.fields:
            return field.name == 'data'

        assert False
