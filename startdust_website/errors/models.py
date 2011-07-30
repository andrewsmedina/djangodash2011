from django.db import models
from datetime import datetime


class Error(models.Model):

    date = models.DateTimeField(default=datetime.now, editable=False)
    url = models.URLField(verify_exists=False)
    traceback = models.TextField()
    exception = models.CharField(max_length=255)

    def __unicode__(self):
        return self.exception
