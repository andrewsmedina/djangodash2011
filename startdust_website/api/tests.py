from django.test import TestCase
from django.contrib.auth.models import User
from errors.models import Error
from responses.models import Response

import base64


class ApiErrorTestCase(TestCase):

    def setUp(self):
        self.user = User(username='username')
        self.user.set_password('password')
        self.user.save()

        auth = '%s:%s' % ('username', 'password')
        auth = 'Basic %s' % base64.encodestring(auth)
        auth = auth.strip()
        self.extra = {
            'HTTP_AUTHORIZATION': auth,
        }

    def tearDown(self):
        self.user.delete()

    def test_api_error_post_view_should_add_a_error(self):
        '''
        api error post should add error
        '''
        post_data = {
            'exception': 'some exception',
            'url': 'http://someurl.com',
            'traceback': 'some traceback',
        }

        self.client.post('/api/error/', post_data, **self.extra)

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

        response = self.client.post('/api/error/', post_data, **self.extra)
        self.assertEqual(200, response.status_code)

    def test_add_error_should_returns_405_when_the_method_isnt_post(self):
        '''
        add_error should returns 405 status code when method isnt a post
        '''
        response = self.client.get('/api/error/', **self.extra)

        self.assertEqual(405, response.status_code)

    def test_add_error_should_returns_methods_allowed_when_the_method_isnt_post(self):
        '''
        add_error should returns 405 status code when method inst a post
        and returns post in method allowed
        '''
        response = self.client.get('/api/error/', **self.extra)
        self.assertTrue('POST' in [method for method in response.items()[2]])

    def test_api_error_should_returns_a_error_if_url_is_empty(self):
        '''
        api error post should returns a error if url is empty
        '''
        post_data = {
            'exception': 'some exception',
            'url': '',
            'traceback': 'some traceback',
        }

        response = self.client.post('/api/error/', post_data, **self.extra)
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

        response = self.client.post('/api/error/', post_data, **self.extra)
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

        response = self.client.post('/api/error/', post_data, **self.extra)
        self.assertEqual(500, response.status_code)

    def test_api_error_should_returns_a_error_if_url_isnt_in_post_dict(self):
        '''i
        api error post should returns a error if url isnt in post dict
        '''
        post_data = {
            'exception': 'some exception',
            'traceback': 'some traceback',
        }

        response = self.client.post('/api/error/', post_data, **self.extra)
        self.assertEqual(500, response.status_code)

    def test_api_error_should_returns_a_error_if_exception_isnot_in_post_dict(self):
        '''
        api error post should returns a error if exception isnot in post dict
        '''
        post_data = {
            'url': 'http://someurl.com',
            'traceback': 'some traceback',
        }

        response = self.client.post('/api/error/', post_data, **self.extra)
        self.assertEqual(500, response.status_code)

    def test_api_error_should_returns_a_error_if_traceback_isnot_in_post_dict(self):
        '''
        api error post should returns a error if traceback isnot in post dict
        '''
        post_data = {
            'exception': 'some exception',
            'url': 'http://someurl.com',
        }

        response = self.client.post('/api/error/', post_data, **self.extra)
        self.assertEqual(500, response.status_code)


class ApiResponseTestCase(TestCase):

    def setUp(self):
        self.user = User(username='username')
        self.user.set_password('password')
        self.user.save()

        auth = '%s:%s' % ('username', 'password')
        auth = 'Basic %s' % base64.encodestring(auth)
        auth = auth.strip()
        self.extra = {
            'HTTP_AUTHORIZATION': auth,
        }

    def tearDown(self):
        self.user.delete()

    def test_api_response_view_should_add_a_response(self):
        '''
        api response post should add response
        '''
        post_data = {
            'time': 0.1123,
            'url': 'http://someurl.com',
            'token': '123',
        }

        response = self.client.post('/api/response/', post_data, **self.extra)
        
        try:
            Response.objects.get(time=post_data['time'])
        except Response.DoesNotExist:
            assert False

    def test_request_api_view_should_returns_200(self):
        '''
        request api should returns 200 if response is added
        '''
        post_data = {
            'time': 0.1123,
            'url': 'http://someurl.com',
            'token': '123',
        }

        response = self.client.post('/api/response/', post_data, **self.extra)
        self.assertEqual(200, response.status_code)

    def test_should_returns_405_when_the_method_isnt_post(self):
        '''
        request api should returns 405 status code when method isnt a post
        '''
        response = self.client.get('/api/response/', **self.extra)
        self.assertEqual(405, response.status_code)

    def test_should_returns_methods_allowed_when_the_method_isnt_post(self):
        '''
        request api should returns 405 status code when method inst a post
        and returns post in method allowed
        '''
        response = self.client.get('/api/response/', **self.extra)
        self.assertTrue('POST' in [method for method in response.items()[2]])

    def test_should_returns_a_error_if_url_is_empty(self):
        '''
        response api should returns a error if url is empty
        '''
        post_data = {
            'time': 0.1123,
            'url': '',
        }

        response = self.client.post('/api/response/', post_data, **self.extra)
        self.assertEqual(500, response.status_code)

    def test_should_returns_a_error_if_url_isnot_in_post_dict(self):
        '''
        response api should returns a error if url isnot in post dict
        '''
        post_data = {
            'time': 0.1124,
        }

        response = self.client.post('/api/response/', post_data, **self.extra)
        self.assertEqual(500, response.status_code)

    def test_should_returns_a_error_if_time_isnot_in_post_dict(self):
        '''
        response api should returns a error if time isnot in post dict
        '''
        post_data = {
            'url': 'http://someulr.com',
        }

        response = self.client.post('/api/response/', post_data, **self.extra)
        self.assertEqual(500, response.status_code)
