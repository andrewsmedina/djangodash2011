from django.conf.urls.defaults import patterns, include, url
from panel.views import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='panel-index'),
    url(r'^projects/(?P<id_project>\d+)/$', 'panel.views.show_project', name='project'),
    url(r'^projects/add/', 'panel.views.add_project', name='add-project'),
	url(r'^projects/(?P<id_project>\d+)/delete/$', 'panel.views.remove_project', name='delete-project'),
)