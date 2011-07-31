from django.db import models


class Request(models.Model):

    url = models.URLField(verify_exists=False)
