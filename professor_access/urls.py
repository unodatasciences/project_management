from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


from . import views


app_name = 'professor_access'

urlpatterns = [
  path ('', views.professor_list, name='pa_list'),
  #path ('1', views.student_list, name='sa_list'),
  path ('new', views.professor_create, name='project_new'),
  #path ('edit/<int:pk>', views.professor_update, name='project_edit'),
  # path ('projects', views.projects, name='projects'),
  path ('detail/<int:pk>', views.detail, name='detail'),
  #path ('detail2/<int:pk>', views.detail2, name='detail2'),
  path ('files', views.files, name='files'),
  path ('upload/<str:filename>', views.upload, name='upload'),
  #path ('mdeditor', include ('mdeditor.urls'))
  #path ('ckeditor/', include('ckeditor_uploader.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
