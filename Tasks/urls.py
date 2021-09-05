from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('register', views.register, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('profile', views.profile, name='profile'),
    path('goals', views.goals, name='goals'),
    path('tasks',views.tasks, name ='tasks'),
    path('expenses', views.expenses, name='expenses')
]