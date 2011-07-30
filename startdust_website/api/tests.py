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

    def test_api_error_post_view_should_returns_200(self):
        '''
        api error post should returns 200 if error is added
        '''
        post_data = {
            'exception': 'some exception',
            'url': 'http://someurl.com',
            'traceback': 'some traceback',
        }

        request = RequestFactory().post('/api/errors/', post_data)
        response = add_error(request)

        self.assertEqual(200, response.status_code)

    def test_add_error_should_returns_405_when_the_method_isnt_post(self):
        '''
        add_error should returns 405 status code when method isnt a post
        '''
        request = RequestFactory().get('/api/errors/')
        response = add_error(request)

        self.assertEqual(405, response.status_code)

    def test_add_error_should_returns_methods_allowed_when_the_method_isnt_post(self):
        '''
        add_error should returns 405 status code when method inst a post
        and returns post in method allowed
        '''
        request = RequestFactory().get('/api/errors/')
        response = add_error(request)

        self.assertTrue('post' in [method for method in response.items()[1]])

    def test_api_error_should_returns_a_error_if_url_is_empty(self):
        '''
        api error post should returns a error if url is empty
        '''
        post_data = {
            'exception': 'some exception',
            'url': '',
            'traceback': 'some traceback',
        }

        request = RequestFactory().post('/api/errors/', post_data)
        response = add_error(request)

        self.assertEqual(500, response.status_code)

    def test_api_error_should_returns_a_error_if_exception_is_empty(self):
        '''
        api error post should returns a error if exception is empty
        '''
        post_data = {
            'exception': '',
            'url': 'http://someurl.com',
            'traceback': 'some traceback',
        }

        request = RequestFactory().post('/api/errors/', post_data)
        response = add_error(request)

        self.assertEqual(500, response.status_code)

    def test_api_error_should_returns_a_error_if_traceback_is_empty(self):
        '''
        api error post should returns a error if traceback is empty
        '''
        post_data = {
            'exception': 'some exception',
            'url': 'http://someurl.com',
            'traceback': '',
        }

        request = RequestFactory().post('/api/errors/', post_data)
        response = add_error(request)

        self.assertEqual(500, response.status_code)

    def test_api_error_should_returns_a_error_if_url_isnt_in_post_dict(self):
        '''i
        api error post should returns a error if url isnt in post dict
        '''
        post_data = {
            'exception': 'some exception',
            'traceback': 'some traceback',
        }

        request = RequestFactory().post('/api/errors/', post_data)
        response = add_error(request)

        self.assertEqual(500, response.status_code)

    def test_api_error_should_returns_a_error_if_exception_isnot_in_post_dict(self):
        '''
        api error post should returns a error if exception isnot in post dict
        '''
        post_data = {
            'url': 'http://someurl.com',
            'traceback': 'some traceback',
        }

        request = RequestFactory().post('/api/errors/', post_data)
        response = add_error(request)

        self.assertEqual(500, response.status_code)

    def test_api_error_should_returns_a_error_if_traceback_isnot_in_post_dict(self):
        '''
        api error post should returns a error if traceback isnot in post dict
        '''
        post_data = {
            'exception': 'some exception',
            'url': 'http://someurl.com',
        }

        request = RequestFactory().post('/api/errors/', post_data)
        response = add_error(request)

        self.assertEqual(500, response.status_code)
