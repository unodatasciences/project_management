from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=50)
    advisor = models.CharField(max_length=200)
    stage = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    note = models.TextField(blank=True)
    def __str__(self):
        return str(self.name)