from django.db import models


class Error(models.Model):

    date = models.DateTimeField()
    url = models.URLField(verify_exists=False)
    traceback = models.TextField()
    exception = models.CharField(max_length=255)

    def __unicode__(self):
        return self.exception
