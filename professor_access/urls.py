from django.urls import path

from . import views


app_name = 'professor_access'

urlpatterns = [
  path ('', views.professor_list, name='pa_list'),
  path ('new', views.professor_create, name='project_new'),
  path('post/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
  path ('edit1/<int:pk>', views.professor_update1, name='project_edit1'),
  #path ('blog', include('blog.urls'), name ='blog'),
  #path ('list', views.post_list, name='post_list'),
  path ('edit/<int:pk>', views.professor_update, name='project_edit'),
  path ('delete/<int:pk>', views.professor_delete, name='project_delete'),

]


