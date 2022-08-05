from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
  title = models.CharField(max_length=255)
  title_tag = models.CharField(max_length=255, default="Blog Post")
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  body = models.TextField()
  create = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.title + '  | ' + str(self.author)
  
  #Após as ações de criar e editar, irá retornar para a paǵina de detail 
  #como se fosse o atributo 'success_url' em views
  def get_absolute_url(self):
    return reverse('detail_post', args=(str(self.id)))
