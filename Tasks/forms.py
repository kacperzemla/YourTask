from Tasks.models import Goal
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Goal
# Create your models here.

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class GoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(GoalForm, self).__init__(*args, **kwargs)