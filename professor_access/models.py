from django.db import models
from django.urls import reverse

class Professor_Project(models.Model):
    name = models.CharField(max_length=50)
    advisor = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    stage = models.CharField(max_length=50)

    def __str__(self):
        return self.name


