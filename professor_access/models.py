from django.db import models
from django.urls import reverse

class Project(models.Model):
    name = models.CharField(max_length=50 )
    details = models.CharField(max_length=200 )
    advisor = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    stage = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


