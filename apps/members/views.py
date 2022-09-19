from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DetailView
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView, LoginView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm, EditProfileForm, CreateProfileForm, LoginForm

from theblog.models import Profile

class LoginInterfaceView(LoginView):
  form_class = LoginForm
  template_name = 'registration/login.html'

class UserRegisterView(CreateView):
  form_class = SignUpForm
  template_name = 'registration/register.html'
  success_url = reverse_lazy('login')

class UserEditSettingsView(LoginRequiredMixin, UpdateView):
  form_class = EditProfileForm
  template_name = 'registration/edit_settings.html'
  login_url = 'login'
  success_url = reverse_lazy('home')

  def get_object(self):
    return self.request.user

#Mostra dados públicos do autor/usuário
class ShowProfilePageView(DetailView):
  model = Profile
  template_name = 'registration/user_profile.html'

  def get_context_data(self, *args, **kwargs):
    user_profile = get_object_or_404(Profile, id=self.kwargs['pk'])
    context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
    context['user_profile'] = user_profile
    return context

class EditProfilePageView(LoginRequiredMixin, UpdateView):
  model = Profile
  template_name = 'registration/edit_user_profile.html'
  login_url = 'login'
  fields = ['bio', 'profile_pic','website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url', 'linkedin_url']
  success_url = reverse_lazy('home')

  def get_context_data(self, *args, **kwargs):
    user_profile = get_object_or_404(Profile, id=self.kwargs['pk'])
    context = super(EditProfilePageView, self).get_context_data(*args, **kwargs)
    context['user_profile'] = user_profile
    return context

class CretaProfilePageView(LoginRequiredMixin, CreateView):
  model = Profile
  template_name = "registration/create_profile.html"
  form_class = CreateProfileForm
  success_url = reverse_lazy('home')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
  template_name = 'registration/password_reset.html'
  email_template_name = 'registration/password_reset_email.html'
  subject_template_name = 'registration/password_reset_subject'
  success_message =  "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
  success_url = reverse_lazy('home')