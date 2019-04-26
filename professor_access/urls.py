from django.urls import path

from . import views


app_name = 'professor_access'

urlpatterns = [
  path ('', views.professor_list, name='pa_list'),
  path ('new', views.professor_create, name='project_new'),
  path ('edit/<int:pk>', views.professor_update, name='project_edit'),
  path ('projects', views.projects, name='projects'),
  path ('detail/<int:pk>', views.detail, name='detail'),
  path ('files', views.files, name='files'),
  path ('upload/<str:filename>', views.upload, name='upload'),

]


