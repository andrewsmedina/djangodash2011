import urllib


STARDUST_URL = 'http://localhost:8000/api'


def send_error_to_server(exception, url, traceback):
    '''
    send error message to stardust server
    '''
    post_dict = {
        'exception': exception,
        'url': url,
        'traceback': traceback,
    }
    
    post_dict = urllib.urlencode(post_dict)
    response = urllib.urlopen('%s/error/' % STARDUST_URL, post_dict).read()
    return response


def send_response_to_server(url, time):
    '''
    send response to stardust server
    '''
    post_dict = {
        'url': url,
        'time': time,
    }

    post_dict = urllib.urlencode(post_dict)
    response = urllib.urlopen('%s/response/' % STARDUST_URL, post_dict).read()
    return response
