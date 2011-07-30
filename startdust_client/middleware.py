from dispatchers import send_error_to_server, send_response_to_server
from multiprocessing import Process
from datetime import datetime

import traceback
import sys


class StartDustMiddleware(object):

    def process_exception(self, request, exception):
        url = 'http://%s%s%s' % (request.META['SERVER_NAME'], ':' + request.META['SERVER_PORT'], request.path_info)
        exc_info = sys.exc_info()
        trace = '\n'.join(traceback.format_exception(*(exc_info or sys.exc_info())))
        proccess = Process(target=send_error_to_server, args=(exception.message, url, trace))
        proccess.start()

    def process_request(self, request):
        request.start = datetime.now()

    def process_response(self, request, response):
        url = 'http://%s%s%s' % (request.META['SERVER_NAME'], ':' + request.META['SERVER_PORT'], request.path_info)
        end = datetime.now()
        time = end - request.start
        proccess = Process(target=send_response_to_server, args=(url, time))
        proccess.start()
        return response
