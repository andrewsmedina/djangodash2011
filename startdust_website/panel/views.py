from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from projects.forms import ProjectForm
from projects.models import Project


class IndexView(TemplateView):
    template_name = 'panel/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context

def show_project(request, id_project):
    return TemplateResponse(request, '/panel/project.html', {})


def add_project(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/panel/')

    else:
        form = ProjectForm()

    return TemplateResponse(request, 'panel/project_form.html', {'form': form})
