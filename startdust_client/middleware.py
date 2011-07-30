import traceback
import sys


class StartDustMiddleware(object):

    def process_exception(self, request, exception):
        exc_info = sys.exc_info()
        #'\n'.join(traceback.format_exception(*(exc_info or sys.exc_info())))
