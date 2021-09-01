from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import templates
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
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

def loginPage(request):

    if request.method  == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'Username OR password is incorrect')
        
    context = {}
    return render(request, 'Tasks/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def profile(request):
    context = {}
    return render(request, 'Tasks/profile.html', context)