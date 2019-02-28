from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from student_access.models import Project


class studentForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'advisor', 'email', 'stage']


def student_list(request, template_name='student_access/sa_list.html'):
    project =Project.objects.all()
    data = {}
    data['object_list'] = project
    return render(request, template_name, data)