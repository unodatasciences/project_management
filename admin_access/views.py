from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from admin_access.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_id','name', 'permission', 'budget', 'stage']


@login_required
def admin_list(request, template_name='admin_access/aa_list.html'):
    if request.user.is_superuser:
        project = Project.objects.all()
    else:
        project = Project.objects.filter(user=request.user)
    data = {}
    data['object_list'] = project
    return render(request, template_name, data)

@login_required
def admin_create(request, template_name='admin_access/project_form.html'):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.user = request.user
        project.save()
        return redirect('admin_access:aa_list')
    return render(request, template_name, {'form':form})

@login_required
def admin_update(request, pk, template_name='admin_access/project_form.html'):
    if request.user.is_superuser:
        project= get_object_or_404(Project, pk=pk)
    else:
        project= get_object_or_404(Project, pk=pk, user=request.user)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('admin_access:aa_list')
    return render(request, template_name, {'form':form})

@login_required
def admin_delete(request, pk, template_name='admin_access/project_confirm_delete.html'):
    if request.user.is_superuser:
        project= get_object_or_404(Project, pk=pk)
    else:
        project= get_object_or_404(Project, pk=pk, user=request.user)
    if request.method=='POST':
        project.delete()
        return redirect('admin_access:aa_list')
    return render(request, template_name, {'object':project})


