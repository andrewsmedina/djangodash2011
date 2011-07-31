from unittest import TestCase
from dispatchers import Dispatcher 


class DispatcherTestCase(TestCase):

    def setUp(self):
        self.dispatcher = Dispatcher('andrews', 'andrews', 'sometoken')

    def test_send_request_to_server(self):
        response = self.dispatcher.send_request('http://someurl.com')
        self.assertEqual('request added with success!', response)

    def test_send_error_to_server(self):
        response = self.dispatcher.send_error('some excpetion', 'http://someurl.com', 'some traceback')
        self.assertEqual('error added with success!', response)

    def test_send_response_to_server(self):
        response = self.dispatcher.send_response('http://someurl.com', 1.234)
        self.assertEqual('response added with success!', response)
