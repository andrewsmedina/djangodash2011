from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home.views import IndexView, DocsView, FeaturesView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^docs/$', DocsView.as_view(), name='docs'),
    url(r'^features/$', FeaturesView.as_view(), name='features'),

    (r'^api/', include('api.urls')),
    (r'^panel/', include('panel.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^auth/', include('registration.auth_urls')),
)

urlpatterns += staticfiles_urlpatterns()
