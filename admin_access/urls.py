from django.urls import path

from . import views

app_name = 'admin_access'

urlpatterns = [
  path('', views.Project, name='aa_list'),

]