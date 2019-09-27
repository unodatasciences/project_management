from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from professor_access.models import Project
from workflow.models import get_role
from .forms import LoginForm
from django.contrib.auth.decorators import login_required, user_passes_test


def student_required(function):
    actual_decorator = user_passes_test(
        lambda u: get_role(u) == 'student',
        login_url='/login/'
    )
    return actual_decorator(function)


@student_required
def dashboard(request):
    return render(request,
                  'student_access/dashboard.html',
                  {'section': 'dashboard'})


@student_required
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
                return redirect("student_access:sa_list")
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    elif request.method == 'GET':
        form = LoginForm ()
        context = {'form': LoginForm}
        return render (request, 'student_access/login.html', context)
    else:
        return HttpResponse ("Use GET to requrest data")


class studentForm(ModelForm):
    class Meta:
        model = Project
        fields = ['id','name', 'advisor', 'stage']


@login_required
def student_list(request, template_name='student_access/sa_list.html'):
    professor = request.user.profile.professor
    project = Project.objects.filter(user=professor)
    #project = Project.objects.filter(user=professor, student_name=request.user.name)
    data = {}
    data['object_list'] = project
    return render(request, template_name, data)


@student_required
def detail(request, pk, template_name='student_access/detail.html'):
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
        return redirect('student_access:sa_list')

    return render(request, template_name, locals())