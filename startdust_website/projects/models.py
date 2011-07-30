from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(verify_exists=False)
    token = models.CharField(max_length=255)
