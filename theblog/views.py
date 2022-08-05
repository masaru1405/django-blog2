from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostForm, EditForm


class HomeView(ListView):
  model = Post
  template_name = 'theblog/home.html'
  context_object_name = 'posts'
  ordering = ['-create']

class PostDetail(DetailView):
  model = Post
  template_name = 'theblog/post_detail.html'
  context_object_name = 'post'

class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  template_name = 'theblog/post_new.html'
  form_class = PostForm
  login_url = 'login'
  #fields = '__all__'
  #success_url = '/'

class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  template_name = 'theblog/post_update.html'
  form_class = EditForm
  login_url = 'login'

class PostDelete(LoginRequiredMixin, DeleteView):
  model = Post
  template_name = 'theblog/post_delete.html'
  success_url = reverse_lazy('home')
  login_url = 'login'