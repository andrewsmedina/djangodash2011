from django.db import models
from datetime import datetime
from projects.models import Project


class Error(models.Model):

    date = models.DateTimeField(default=datetime.now, editable=False)
    url = models.URLField(verify_exists=False)
    traceback = models.TextField()
    exception = models.CharField(max_length=255)
    project = models.ForeignKey(Project, null=True, editable=False) #will be change this

    def __unicode__(self):
        return self.exception
