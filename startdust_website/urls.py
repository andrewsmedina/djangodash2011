from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home.views import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),

    (r'^api/', include('api.urls')),
    (r'^panel/', include('panel.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^auth/', include('registration.auth_urls')),
)

urlpatterns += staticfiles_urlpatterns()
