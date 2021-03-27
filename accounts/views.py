from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import MyUserCreationForm

class RegisterViews(CreateView):
    form_class = MyUserCreationForm
    template_name = 'accounts/register.html'
    success_url = '/login/'