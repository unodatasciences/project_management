import os
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.forms import ModelForm


from professor_access.models import Project
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

from django.contrib.admin.views.decorators import staff_member_required



class professorForm(ModelForm):
    class Meta:
        model = Project
        fields = ['id','name', 'student_name', 'stage']

@staff_member_required
def professor_list(request, template_name='professor_access/pa_list.html'):
    project = Project.objects.all()
    data = {}
    data['object_list'] = project
    return render(request, template_name, data)

@login_required
def student_list(request, template_name='professor_access/sa_list.html'):
    project =Project.objects.all()
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
        project.student_name= student_name
        project.stage = stage
        project.description = description
        project.note = note

        project.save()
        return redirect('professor_access:pa_list')

    return render(request, template_name, locals())


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


def files(request, template_name='professor_access/files.html'):
    project = Project.objects.all()
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

def upload(request, filename):
    path = os.path.join('upload', filename)
    return HttpResponse(open(path, 'rb').read())

@login_required
class studentForm(ModelForm):
    class Meta:
        model = Project
        fields = ['id','name', 'advisor', 'stage']

def student_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user:
                login(request, user)
                return redirect("professor_access:sa_list")
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    elif request.method == 'GET':
        form = LoginForm ()
        context = {'form': LoginForm}
        return render (request, 'professor_access/login.html', context)
    else:
        return HttpResponse ("Use GET to requrest data")

