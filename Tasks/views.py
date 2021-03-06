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
from .forms import GoalForm, TaskForm

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
    tasks = request.user.customer.task_set.all()
    customer = request.user.customer
    task = Task(customer=customer)
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')

    context = {
        'form': form, 'tasks': tasks
    }

    return render(request, 'Tasks/tasks.html', context)

@login_required(login_url='login')
def goals(request):

    goals = request.user.customer.goal_set.all()

    customer = request.user.customer
    goal = Goal(customer = customer)
    form = GoalForm()

    if request.method == "POST":
        form = GoalForm(request.POST, instance = goal)
        if form.is_valid():
            form.save()
            return redirect('goals')

    context = {
        'form': form, 'goals': goals
    }

    return render(request, 'Tasks/goals.html', context)

@login_required(login_url='login')
def updateGoal(request,goal_id):
    goal = Goal.objects.get(pk = goal_id)
    if goal.complete == True:
        goal.complete = False
    else:
        goal.complete = True
    goal.save()


    return redirect('goals')

@login_required(login_url='login')
def updateTask(request,pk):
    task = Task.objects.get(pk=pk)
    if task.complete == True:
        task.complete = False
    else:
        task.complete = True
        
    task.save()
    return redirect('tasks')


@login_required(login_url='login')
def expenses(request):
    context = {

    }

    return render(request, 'Tasks/expenses.html', context)

@login_required(login_url='login')
def deleteGoals(request):
    goals = request.user.customer.goal_set.all()
    for i in goals:
        if(i.complete == True):
            i.delete()
    
    return redirect('goals')