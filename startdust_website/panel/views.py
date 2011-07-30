from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from projects.forms import ProjectForm
from projects.models import Project
from errors.models import Error


class IndexView(TemplateView):
    template_name = 'panel/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['errors'] = Error.objects.all()
        return context

def show_project(request, id_project):
    project = Project.objects.get(id=id_project)
    project_content = {'name': project.name,
                       'url': project.url}

    return TemplateResponse(request, '/panel/project.html', {'project': project_content})


def add_project(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/panel/')

    else:
        form = ProjectForm()

    return TemplateResponse(request, 'panel/project_form.html', {'form': form})
