from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def demo(request):
    temp=loader.get_template('grid 4.html')
    return HttpResponse(temp.render())

