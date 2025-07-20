from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Student

def testing(request):
  mydata = Student.objects.all()
  template = loader.get_template('temp.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))