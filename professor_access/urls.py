from django.urls import path

from . import views


app_name = 'professor_access'

urlpatterns = [
  path ('', views.professor_list, name='pa_list'),
  path ('new', views.professor_create, name='project_new'),
  path ('edit1/<int:pk>', views.professor_update1, name='project_edit1'),
  path ('edit/<int:pk>', views.professor_update, name='project_edit'),
  path ('delete/<int:pk>', views.professor_delete, name='project_delete'),

]


