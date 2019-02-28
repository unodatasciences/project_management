from django.db import models
from django.urls import reverse


#class Project(models.Model):
#    name = models.CharField(max_length=200)
#    pages = models.IntegerField()

#    def __str__(self):
#        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50)
    permission = models.CharField (max_length=50)
    budget = models.IntegerField(blank=False, null=False)
    stage = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)