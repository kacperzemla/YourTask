from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import templates
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.
def index(request):
    context = {}
    return render(request, 'Tasks/main.html', context)
    
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'Tasks/register.html', context)

def login(request):
    context = {}
    return render(request, 'Tasks/login.html', context)