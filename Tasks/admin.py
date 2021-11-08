from django.contrib import admin
from .models import Goal, Customer, Task
# Register your models here.

admin.site.register(Goal)
admin.site.register(Customer)
admin.site.register(Task)