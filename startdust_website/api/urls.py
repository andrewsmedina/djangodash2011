from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from api.handlers import ErrorHandler, ResponseHandler, RequestHandler


auth = HttpBasicAuthentication(realm="stardust")
ad = {'authentication': auth}

error_resource = Resource(handler=ErrorHandler, **ad)
response_resource = Resource(handler=ResponseHandler, **ad)
request_resource = Resource(handler=RequestHandler, **ad)

error_resource.csrf_exempt = True
response_resource.csrf_exempt = True
request_resource.csrf_exempt = True


urlpatterns = patterns('',
    url(r'^error/$', error_resource),
    url(r'^response/$', response_resource),
    url(r'^request/$', request_resource),
)
