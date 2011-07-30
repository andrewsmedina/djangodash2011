from uuid import uuid4
from django.forms import ModelForm
from projects.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('token')

    def save(self):
        obj = super(ProjectForm, self).save(commit=False)
        obj.token = str(uuid4())
        obj.save()
        return obj

