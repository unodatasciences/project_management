from django.urls import path

from . import views

app_name = 'admin_access'

urlpatterns = [
  path('', views.admin_list, name='aa_list'),

]