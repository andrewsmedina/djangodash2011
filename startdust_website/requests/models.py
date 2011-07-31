from django.db import models
from datetime import datetime
from projects.models import Project


class Request(models.Model):

    url = models.URLField(verify_exists=False)
    date = models.DateTimeField(null=True, editable=False)
    project = models.ForeignKey(Project, null=True, editable=False)

    class Meta:
        ordering = ['date']

    def save(self, *args, **kwargs):
        date = datetime.now()
        self.date = datetime(date.year, date.month, date.day, date.hour, date.minute)
        super(Request, self).save(*args, **kwargs)
