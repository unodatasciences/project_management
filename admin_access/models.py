from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

class Project(models.Model):
    project_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    advisor = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    stage = models.CharField(max_length=50)

    def __str__(self):
        return str(self.project_id)

