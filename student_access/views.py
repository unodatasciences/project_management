from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from student_access.models import Project
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request,
                  'student_access/dashboard.html',
                  {'section': 'dashboard'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'student_access/login.html', {'form': form})


#@login_required
class studentForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'advisor', 'email', 'stage']

#@login_required
def student_list(request, template_name='student_access/sa_list.html'):
    project =Project.objects.all()
    data = {}
    data['object_list'] = project
    return render(request, template_name, data)