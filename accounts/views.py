from django.contrib import auth
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth import authenticate, login

from .forms import MyUserCreationForm,MyAuthenticationForm

class RegisterViews(CreateView):
    form_class = MyUserCreationForm
    template_name = 'accounts/register.html'
    success_url = '/login/'

class LoginView(FormView):
    form_class = MyAuthenticationForm
    success_url = '/'
    template_name = 'accounts/login.html'
    default_next = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username,password=password)
        if user :
            login(self.request,user)
        return super(LoginView,self).form_valid(form)
