from django.db import models


class Response(models.Model):

    time = models.IntegerField()
    url = models.URLField(verify_exists=False)
