from django.urls import include, path
from django.contrib import admin

from workflow import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_access/', include('student_access.urls', namespace='student_access')),
    #path('student_access/login/', include ('student_access.urls', namespace='login')),
    path('professor_access/', include('professor_access.urls', namespace='professor_access')),
    path('admin_access/', include('admin_access.urls', namespace='admin_access')),
    path('', views.home),

]

