from django.db import models
from datetime import datetime


class Response(models.Model):

    time = models.IntegerField()
    url = models.URLField(verify_exists=False)
    date = models.DateTimeField(default=datetime.now, editable=False)
