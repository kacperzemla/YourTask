from django import forms
from django.db import models
from django.contrib.auth.models import User
import datetime

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    name = models.CharField(max_length=200 ,null = True)
    phone = models.CharField(max_length=200, null = True)
    # email = models.CharField(max_length=200, null = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.name

class Goal(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Task(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.text