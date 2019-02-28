from django.urls import path

from . import views

app_name = 'student_access'

urlpatterns = [
  path('', views.Project, name='sa_list'),

]
