import urllib2
import urllib
import base64


STARDUST_URL = 'http://localhost:8000/api'


class Dispatcher(object):

    def authenticate(self, url):
        '''
        add authorization information to header
        '''
        request = urllib2.Request(url)
        base64string = base64.encodestring('%s:%s' % ('andrews', 'andrews'))[:-1]
        authheader =  "Basic %s" % base64string
        request.add_header("Authorization", authheader)
        return request

    def send(self, url, post_dict):
        '''
        send a post to url
        '''
        request = self.authenticate(url)
        post_dict = urllib.urlencode(post_dict)
        response = urllib2.urlopen(request, post_dict).read()
        return response

    def send_error(self, exception, url, traceback):
        '''
        send error message to stardust server
        '''
        post_dict = {
            'exception': exception,
            'url': url,
            'traceback': traceback,
        }

        error_url = '%s/error/' % STARDUST_URL
        return self.send(error_url, post_dict)

    def send_response(self, url, time):
        '''
        send response to stardust server
        '''
        post_dict = {
            'url': url,
            'time': time,
        }

        response_url = '%s/response/' % STARDUST_URL
        return self.send(response_url, post_dict)
