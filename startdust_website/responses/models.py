from django.db import models
from datetime import datetime
from projects.models import Project

class Response(models.Model):

    time = models.FloatField()
    url = models.URLField(verify_exists=False)
    date = models.DateTimeField(null=True, editable=False)
    project = models.ForeignKey(Project, null=True, editable=False) #will be change this

    class Meta:
        ordering = ['date']

    def save(self, *args, **kwargs):
        date = datetime.now()
        self.date = datetime(date.year, date.month, date.day, date.hour, date.minute, date.second)
        super(Response, self).save(*args, **kwargs)
