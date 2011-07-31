from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(verify_exists=False)
    token = models.CharField(max_length=255)
    user = models.ManyToManyField(User, null=True, blank=True)
