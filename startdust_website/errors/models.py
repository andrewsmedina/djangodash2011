from django.db import models


class Error(models.Model):
    date = models.DateTimeField()
    url = models.URLField(verify_exists=False)
