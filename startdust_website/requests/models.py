from django.db import models
from datetime import datetime


class Request(models.Model):

    url = models.URLField(verify_exists=False)
    date = models.DateTimeField(default=datetime.now, editable=False)
