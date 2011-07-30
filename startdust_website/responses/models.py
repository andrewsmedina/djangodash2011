from django.db import models
from datetime import datetime
from projects.models import Project


class Response(models.Model):

    time = models.IntegerField()
    url = models.URLField(verify_exists=False)
    date = models.DateTimeField(default=datetime.now, editable=False)
    project = models.ForeignKey(Project, null=True, editable=False) #will be change this
