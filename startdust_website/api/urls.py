from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^error/$', 'api.views.add_error', name='api-add-error'),
)
