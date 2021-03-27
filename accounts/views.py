from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import AuthenticationForm

from .forms import MyUserCreationForm,MyAuthenticationForm

class RegisterViews(CreateView):
    form_class = MyUserCreationForm
    template_name = 'accounts/register.html'
    success_url = '/login/'

class LoginView(FormView):
    form_class = MyAuthenticationForm
    success_url = '/'
    template_name = 'accounts/login.html'