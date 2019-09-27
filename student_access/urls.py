from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'student_access'

urlpatterns = [
  path ('', views.student_list, name='sa_list'),
  #path ('1', views.student_list, name='sa_list'),
  path ('detail/<int:pk>', views.detail, name='detail'),
  #path ('detail2/<int:pk>', views.detail2, name='detail2'),
  #path ('login/', views.student_login, name='login'),
  #path ('login/', auth_views.LoginView.as_view (), name='login'),
  #path ('logout/', auth_views.LogoutView.as_view (), name='logout'),
  #path ('', views.dashboard, name='dashboard'),
  #path ('', views.user_login, name='login'),

]
