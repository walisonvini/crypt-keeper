from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'auth/login.html'

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')

