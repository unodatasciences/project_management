from django.urls import path

from . import views

app_name = 'admin_access'

urlpatterns = [
  path('', views.aa_list, name='aa_list'),

]