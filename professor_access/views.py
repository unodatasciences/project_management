from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.forms import ModelForm

from professor_access.models import Project


class professorForm(ModelForm):
    class Meta:
        model = Project
        fields = ['id','name', 'instructor', 'email', 'stage']

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
        instructor = request.POST['instructor']
        email = request.POST['email']
        stage = request.POST['stage']
        date = request.POST['date']
        background = request.POST['background']

        project.name = name
        project.instructor = instructor
        project.email = email
        project.stage = stage
        project.date = date
        project.background = background
        project.save()
        return redirect('professor_access:projects')

    return render(request, template_name, locals())