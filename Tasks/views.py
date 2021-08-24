from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from . import templates
# Create your views here.
def index(request):
    context = {}
    return render(request, 'Tasks/main.html', context)
    
def register(request):
    context = {
    }
    return render(request, 'Tasks/register.html', context)
