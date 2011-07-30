import urllib


STARDUST_URL = 'http://localhost:8000/api/error/'


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
    response = urllib.urlopen(STARDUST_URL, post_dict).read()
    return response
