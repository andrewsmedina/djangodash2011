from django.db import models
from datetime import datetime
from projects.models import Project


class Request(models.Model):

    url = models.URLField(verify_exists=False)
    date = models.DateTimeField(default=datetime.now, editable=False)
    project = models.ForeignKey(Project, null=True, editable=False)

    class Meta:
        ordering = ['date']
