from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

from datetime import datetime, date

class Category(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name
  
  #https://stackoverflow.com/questions/36330677/django-model-set-default-charfield-in-lowercase
  def save(self, *args, **kwargs):
    self.name = self.name.lower()
    return super(Category, self).save(*args, **kwargs)
  
  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

class Post(models.Model):
  title = models.CharField(max_length=255)
  title_tag = models.CharField(max_length=255, default="Blog Post")
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
  body = models.TextField()
  create = models.DateField(auto_now_add=True)
  category = models.CharField(max_length=255, default='coding')
  likes = models.ManyToManyField(User, related_name='blog_posts')

  def __str__(self):
    return self.title + '  | ' + str(self.author)
  
  def total_likes(self):
    return self.likes.count()
  
  #Após as ações de criar e editar, irá retornar para a paǵina de detail 
  #como se fosse o atributo 'success_url' em views
  def get_absolute_url(self):
    return reverse('detail_post', args=[str(self.id)])


