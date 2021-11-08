from Tasks.models import Goal
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django import contrib, forms
from django.contrib.auth.models import User
from .models import *
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

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'date']
        widgets = {'date': DateInput()}