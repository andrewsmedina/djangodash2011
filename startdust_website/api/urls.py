from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from api.handlers import ErrorHandler

error_resource = Resource(handler=ErrorHandler)

error_resource.csrf_exempt = True

urlpatterns = patterns('',
    url(r'^error/$', error_resource),
)
