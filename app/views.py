from django.shortcuts import render
from app.models import *
from django.views.generic import TemplateView,ListView
# Create your views here.
class Home(TemplateView):
    template_name='app/home.html'

class School_List(ListView):
    model=School
    context_object_name='schools'