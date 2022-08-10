from django import forms
from .models import Post, Category

categories = Category.objects.all().values_list('name', 'name')
categories_list = []

for item in categories:
  categories_list.append(item)

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image'] #tá pegando do model. Já no forms.py de members, estamos criando ali msm no form

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title here'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'userid', 'type': 'hidden'}),
      #'author': forms.Select(attrs={'class': 'form-select'}),
      'category': forms.Select(choices=categories_list,attrs={'class': 'form-select'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
      'snippet': forms.Textarea(attrs={'class': 'form-control'})
    }

class EditForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'title_tag', 'body', 'snippet', 'header_image']

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title here'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
      'snippet': forms.Textarea(attrs={'class': 'form-control'})
    }