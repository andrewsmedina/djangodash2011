from dispatchers import send_error_to_server

import traceback
import sys


class StartDustMiddleware(object):

    def process_exception(self, request, exception):
        url = 'http://%s%s%s' % (request.META['SERVER_NAME'], ':' + request.META['SERVER_PORT'], request.path_info)
        exc_info = sys.exc_info()
        trace = '\n'.join(traceback.format_exception(*(exc_info or sys.exc_info())))
        send_error_to_server(exception.message, url, trace)
