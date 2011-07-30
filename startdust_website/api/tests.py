from django.test import TestCase
from django.test.client import RequestFactory
from api.views import add_error
from errors.models import Error


class ApiPostErrorViewTestCase(TestCase):

    def test_api_error_post_view_should_add_a_error(self):
        '''
        api error post should add error
        '''
        post_data = {
            'exception': 'some exception',
            'url': 'http://someurl.com',
            'traceback': 'some traceback',
        }

        request = RequestFactory().post('/api/errors/', post_data)
        add_error(request)

        try:
            Error.objects.get(exception=post_data['exception'])
        except Error.DoesNotExist:
            assert False
