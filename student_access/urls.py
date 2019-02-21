from django.urls import path

from . import views

app_name = 'student_access'

urlpatterns = [
  path('', views.sa_list, name='sa_list'),

]
