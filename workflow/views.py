from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from workflow.models import UserProfile


def home(request):
    for user in User.objects.all ():
        if not hasattr (user, 'profile'):
            UserProfile.objects.create (user=user)
    return render (request, "home.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        user = auth.authenticate (username=username, password=password)
        if user is not None and user.is_active:
            auth.login (request, user)
            url = f'/{user.profile.role}_access/'
            return HttpResponseRedirect (url)
        else:
            msg = 'Invalid password'

    return render (request, "login.html", locals ())


def register(request):
    if request.method == 'POST':
        username = request.POST.get ('username')
        password1 = request.POST.get ('password1')
        password2 = request.POST.get ('password2')
        role = request.POST.get ('role')
        professor_id = request.POST.get ('professor_id')
        if password1 != password2:
            msg = 'Two password not match'
        elif User.objects.filter (username=username).exists ():
            msg = 'The username is exists'
        else:
            u = User.objects.create (username=username)
            u.set_password (password1)
            u.save ()
            profile = UserProfile.objects.create (user=u)
            profile.role = role
            if role == 'student':
                profile.professor_id = professor_id
            profile.save ()
            return HttpResponseRedirect ('/login/')

    professors = User.objects.filter (profile__role='professor').all ()

    return render (request, "register.html", locals ())

