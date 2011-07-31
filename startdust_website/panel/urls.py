from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required
from panel.views import IndexView

urlpatterns = patterns('',
    url(r'^$', login_required(IndexView.as_view()), name='panel-index'),
    url(r'^projects/(?P<id_project>\d+)/$', 'panel.views.show_project', name='project'),
    url(r'^projects/add/', 'panel.views.add_project', name='add-project'),
	url(r'^projects/(?P<id_project>\d+)/delete/$', 'panel.views.remove_project', name='delete-project'),
    url(r'^projects/(?P<id_project>\d+)/update/$', 'panel.views.change_project', name='update-project')
)
