from django.db import models
from django.urls import reverse
from django.utils import timezone

def current_date():
    return timezone.localdate()

class Project(models.Model):
    name = models.CharField(max_length=50 )
    instructor = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    stage = models.CharField(max_length=50)
    date = models.DateField(default=current_date)
    background = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)


