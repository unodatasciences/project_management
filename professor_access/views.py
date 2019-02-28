from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm


from professor_access.models import Professor_Project

class professorForm(ModelForm):
    class Meta:
        model = Professor_Project
        fields = ['name', 'advisor', 'email', 'stage']



def professor_list(request, template_name='professor_access/pa_list.html'):
    project = Professor_Project.objects.all()
    data = {}
    data['object_list'] = project
    return render(request, template_name, data)