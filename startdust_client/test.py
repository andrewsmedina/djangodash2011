from unittest import TestCase
from dispatchers import Dispatcher 


class SendErrorToServerTestCase(TestCase):

    def test_send_error_to_server(self):
        dispatcher = Dispatcher('andrews', 'andrews', 'sometoken')
        response = dispatcher.send_error('some excpetion', 'http://someurl.com', 'some traceback')
        self.assertEqual('error added with success!', response)


class SendResponseToServerTestCase(TestCase):

    def test_send_response_to_server(self):
        dispatcher = Dispatcher('andrews', 'andrews', 'sometoken')
        response = dispatcher.send_response('http://someurl.com', 1.234)
        self.assertEqual('response added with success!', response)
