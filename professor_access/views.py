from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.forms import ModelForm

from professor_access.models import Project


class professorForm(ModelForm):
    class Meta:
        model = Project
        fields = ['id','name', 'student_name', 'stage']

def professor_list(request, template_name='professor_access/pa_list.html'):
    project = Project.objects.all()
    data = {}
    data['object_list'] = project
    return render(request, template_name, data)



def professor_create(request, template_name='professor_access/project_form.html'):
    form = professorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('professor_access:pa_list')
    return render(request, template_name, {'form':form})


def professor_update(request, pk, template_name='professor_access/project_form.html'):
    project= get_object_or_404(Project, pk=pk)
    form = professorForm(request.POST or None, instance= project)
    if form.is_valid():
        form.save()
        return redirect('professor_access:pa_list')
    return render(request, template_name, {'form':form})

def projects(request, template_name='professor_access/projects.html'):
    project = Project.objects.all()
    data = {}
    data['object_list'] = project
    return render(request, template_name, data)


def detail(request, pk, template_name='professor_access/detail.html'):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        name = request.POST['name']
        student_name = request.POST['student_name']
        stage = request.POST['stage']
        description = request.POST['description']
        note = request.POST['note']


        project.name = name
        project.instructor = student_name
        project.stage = stage
        project.description = description
        project.note = note
        project.save()
        return redirect('professor_access:pa_list')

    return render(request, template_name, locals())