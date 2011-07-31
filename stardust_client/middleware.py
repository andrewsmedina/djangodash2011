from django.conf import settings
from dispatchers import Dispatcher
from multiprocessing import Process
from datetime import datetime

import traceback
import sys


class StartDustMiddleware(object):

    def __init__(self):
        username = settings.STARDUST_USERNAME
        password = settings.STARDUST_PASSWORD
        token = settings.STARDUST_PROJECT_TOKEN
        self.dispatcher = Dispatcher(username, password, token)

    def process_exception(self, request, exception):
        url = 'http://%s%s%s' % (request.META['SERVER_NAME'], ':' + request.META['SERVER_PORT'], request.path_info)
        exc_info = sys.exc_info()
        trace = '\n'.join(traceback.format_exception(*(exc_info or sys.exc_info())))
        proccess = Process(target=self.dispatcher.send_error, args=(exception.message, url, trace))
        proccess.start()

    def process_request(self, request):
        url = 'http://%s%s%s' % (request.META['SERVER_NAME'], ':' + request.META['SERVER_PORT'], request.path_info)
        proccess = Process(target=self.dispatcher.send_request, args=(url,))
        proccess.start()
        request.start = datetime.now()

    def process_response(self, request, response):
        if hasattr(request, 'start'):
            url = 'http://%s%s%s' % (request.META['SERVER_NAME'], ':' + request.META['SERVER_PORT'], request.path_info)
            end = datetime.now()
            time = end - request.start
            time_in_milliseconds = time.microseconds / 1000.0
            proccess = Process(target=self.dispatcher.send_response, args=(url, time_in_milliseconds))
            proccess.start()
        return response
