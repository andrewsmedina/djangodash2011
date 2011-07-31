import urllib2
import urllib
import base64


STARDUST_URL = 'http://localhost:8000/api'


class Dispatcher(object):

    def send_error(self, exception, url, traceback):
        '''
        send error message to stardust server
        '''
        post_dict = {
            'exception': exception,
            'url': url,
            'traceback': traceback,
        }
        request = urllib2.Request('%s/error/' % STARDUST_URL)
        base64string = base64.encodestring('%s:%s' % ('andrews', 'andrews'))[:-1]
        authheader =  "Basic %s" % base64string
        request.add_header("Authorization", authheader)
        post_dict = urllib.urlencode(post_dict)
        response = urllib2.urlopen(request, post_dict).read()
        return response

    def send_response(self, url, time):
        '''
        send response to stardust server
        '''
        post_dict = {
            'url': url,
            'time': time,
        }
        request = urllib2.Request('%s/response/' % STARDUST_URL)
        base64string = base64.encodestring('%s:%s' % ('andrews', 'andrews'))[:-1]
        authheader =  "Basic %s" % base64string
        request.add_header("Authorization", authheader)

        post_dict = urllib.urlencode(post_dict)
        response = urllib2.urlopen(request, post_dict).read()
        return response
