from django.db import models
from django.urls import reverse
from django.utils import timezone

def current_date():
    return timezone.localdate()

class Project(models.Model):
    name = models.CharField(max_length=50 )
    student_name = models.CharField(max_length=200)
    stage = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)


