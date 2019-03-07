from django.urls import path

from . import views

app_name = 'admin_access'

urlpatterns = [
  path('', views.admin_list, name='aa_list'),
  path ('new', views.admin_create, name='project_new'),
  path ('edit/<int:pk>', views.admin_update, name='project_edit'),
  path ('delete/<int:pk>', views.admin_delete, name='project_delete'),

]