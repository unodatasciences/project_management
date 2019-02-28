from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

class professor_Project(models.Model):
    name = models.CharField(max_length=50)
    advisor = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    stage = models.CharField(max_length=50)

    def __str__(self):
        return self.name

