from django.db import models
from django.urls import reverse
from django.utils import timezone
#from mdeditor.fields import MDTextField
#from ckeditor.fields import RichTextField
#from tinymce.models import HTMLField
#from ckeditor_uploader.fields import RichTextUploadingField



def current_date():
    return timezone.localdate()

class Project(models.Model):
    name = models.CharField(max_length=50 )
    student_name = models.CharField(max_length=200)
    advisor = models.CharField (max_length=200)
    stage = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    note = models.CharField(max_length=5000)
    #note = RichTextUploadingField()
    #note = HTMLField ()
    #note = RichTextField()
    #file = models.FileField(upload_to='upload', blank=True, null=True)
    #test=MDTextField()
    def __str__(self):
        return str(self.id)


    #@property
    #def file_name(self):
    #    if self.file:
    #        return self.file.name.split('/')[-1]
    #    return ''

    #@property
    #def file_url(self):
    #    if self.file:
    #        return self.file.url
    #    return ''

class Project2 (models.Model):
    name = models.CharField (max_length=50)
    advisor = models.CharField (max_length=200)
    stage = models.CharField (max_length=50)
    description = models.CharField(max_length=5000)
    note = models.CharField(max_length=5000)

    def __str__(self):
        return str (self.name)

#class ExampleModel(models.Model):
#    name = models.CharField(max_length=10000)
#    content = MDTextField()

