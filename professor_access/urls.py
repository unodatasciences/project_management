from django.urls import path

from . import views

app_name = 'professor_access'

urlpatterns = [
  path('', views.Professor_Project, name='pa_list'),

]