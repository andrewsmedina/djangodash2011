from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from api.handlers import ErrorHandler, ResponseHandler


error_resource = Resource(handler=ErrorHandler)
response_resource = Resource(handler=ResponseHandler)

error_resource.csrf_exempt = True
response_resource.csrf_exempt = True


urlpatterns = patterns('',
    url(r'^error/$', error_resource),
    url(r'^response/$', response_resource),
)
