from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from admin_access.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'permission', 'budget', 'stage']


@login_required
def aa_list(request, template_name='admin_access:aa_list'):
    if request.user.is_superuser:
        project = Project.objects.all()
    else:
        project = Project.objects.filter(user=request.user)
    data = {}
    data['object_list'] = project
    return render(request, template_name, data)
