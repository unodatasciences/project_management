import os

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.forms import ModelForm

from professor_access.models import Project
from workflow.models import get_role
from .forms import LoginForm
from django.contrib.auth.decorators import user_passes_test


def professor_required(function):
    actual_decorator = user_passes_test(
        lambda u: get_role(u) == 'professor',
        login_url='/login/'
    )
    return actual_decorator(function)


class professorForm(ModelForm):
    class Meta:
        model = Project
        fields = ['id', 'name', 'student_name', 'stage']


@professor_required
def professor_list(request, template_name='professor_access/pa_list.html'):
    project = Project.objects.filter(user=request.user)
    data = {}
    data['object_list'] = project
    return render(request, template_name, data)


@professor_required
def student_list(request, template_name='professor_access/sa_list.html'):
    project = Project.objects.filter(user=request.user)
    data = {}
    data['object_list'] = project
    return render(request, template_name, data)


@professor_required
def professor_create(request, template_name='professor_access/project_form.html'):
    students = User.objects.filter(profile__professor=request.user)
    form = professorForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.user = request.user
        project.advisor = request.user.username
        project.save()
        return redirect('professor_access:pa_list')
    return render(request, template_name, locals())


@professor_required
def professor_update(request, pk, template_name='professor_access/project_form.html'):
    project = get_object_or_404(Project, pk=pk)
    form = professorForm(request.POST or None, instance= project)
    if form.is_valid():
        form.save()
        return redirect('professor_access:pa_list')
    return render(request, template_name, {'form':form})

# @professor_required
# def projects(request, template_name='professor_access/projects.html'):
#     project = Project.objects.all()
#     data = {}
#     data['object_list'] = project
#     return render(request, template_name, data)


@professor_required
def detail(request, pk, template_name='professor_access/detail.html'):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        name = request.POST['name']
        student_name = request.POST['student_name']
        stage = request.POST['stage']
        description = request.POST['description']
        note = request.POST['note']

        project.name = name
        project.student_name = student_name
        project.stage = stage
        project.description = description
        project.note = note

        project.save()
        return redirect('professor_access:pa_list')

    return render(request, template_name, locals())


@professor_required
def detail2(request, pk, template_name='professor_access/detail2.html'):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        name = request.POST['name']
        advisor = request.POST['advisor']
        stage = request.POST['stage']
        description = request.POST['description']
        note = request.POST['note']

        project.name = name
        project.instructor = advisor
        project.stage = stage
        project.description = description
        project.note = note
        project.save()
        return redirect('professor_access:sa_list')

    return render(request, template_name, locals())


@professor_required
def files(request, template_name='professor_access/files.html'):
    project = Project.objects.filter(user=request.user)
    data = {}
    data['object_list'] = project

    if request.method == 'POST':
        id = request.POST['id']
        file = request.FILES.get('file')
        if file:
            project = Project.objects.get(id=id)
            project.file = file
            project.save()
            return redirect('professor_access/files')

    return render(request, template_name, data)


@professor_required
def upload(request, filename):
    path = os.path.join('upload', filename)
    return HttpResponse(open(path, 'rb').read())


class studentForm(ModelForm):
    class Meta:
        model = Project
        fields = ['id','name', 'advisor', 'stage']

