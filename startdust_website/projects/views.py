from django.template.response import TemplateResponse
from projects.forms import ProjectForm

def add_project(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            return

    else:
        form = ProjectForm()

    return TemplateResponse(request, 'project_form.html', {'form': form})
