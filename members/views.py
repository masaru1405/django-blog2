from django.shortcuts import render
from django.views.generic import CreateView
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.urls import reverse_lazy

class UserRegisterView(CreateView):
  form_class = SignUpForm
  template_name = 'registration/register.html'
  success_url = reverse_lazy('login')
