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
    file = models.FileField(upload_to='upload', blank=True, null=True)

    def __str__(self):
        return str(self.id)


    @property
    def file_name(self):
        if self.file:
            return self.file.name.split('/')[-1]
        return ''

    @property
    def file_url(self):
        if self.file:
            return self.file.url
        return ''
