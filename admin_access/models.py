from django.db import models
from django.urls import reverse
from django.conf import settings


class Project(models.Model):
    project_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    permission = models.CharField (max_length=50)
    budget = models.CharField(max_length=200)
    stage = models.CharField(max_length=50)

    def __str__(self):
        return str(self.project_id)

    def get_absolute_url(self):
        return reverse('admin_access:project_edit', kwargs={'pk': self.pk})

