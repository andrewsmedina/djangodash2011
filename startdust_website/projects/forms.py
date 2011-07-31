from uuid import uuid4
from django.forms import ModelForm
from projects.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('token', 'user')

class UpdateProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('token')
