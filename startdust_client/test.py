from unittest import TestCase
from dispatchers import send_error_to_server, send_response_to_server


class SendErrorToServerTestCase(TestCase):

    def test_send_error_to_server(self):
        response = send_error_to_server('some excpetion', 'http://someurl.com', 'some traceback')
        self.assertEqual('error added with success!', response)


class SendResponseToServerTestCase(TestCase):

    def test_send_response_to_server(self):
        response = send_response_to_server('http://someurl.com', 1.234)
        self.assertEqual('response added with success!', response)
