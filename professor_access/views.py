from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from professor_access.models import professor_Project

class student_access_List(ListView):
    model = professor_Project