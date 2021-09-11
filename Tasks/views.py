# from Tasks.models import Customer
from Tasks.decorators import unauthenticated_user
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import templates
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required

from .models import *
# Create your views here.
def index(request):
    context = {}
    return render(request, 'Tasks/main.html', context)

@unauthenticated_user
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(
                user=user,
                name = user.username,
            )
            return redirect('login')
           
    context = {
        'form': form
    }
    return render(request, 'Tasks/register.html', context)

@unauthenticated_user
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

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    context = {}
    return render(request, 'Tasks/profile.html', context)

@login_required(login_url='login')
def tasks(request):
    context = {

    }

    return render(request, 'Tasks/tasks.html', context)

@login_required(login_url='login')
def goals(request):
    context = {

    }

    return render(request, 'Tasks/goals.html', context)

@login_required(login_url='login')
def expenses(request):
    context = {

    }

    return render(request, 'Tasks/expenses.html', context)