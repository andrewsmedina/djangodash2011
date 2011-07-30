from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from projects.forms import ProjectForm


class IndexView(TemplateView):
    template_name = 'panel/index.html'


def add_project(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/panel/')

    else:
        form = ProjectForm()

    return TemplateResponse(request, 'panel/project_form.html', {'form': form})
