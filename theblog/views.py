from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm


class HomeView(ListView):
  model = Post
  template_name = 'theblog/home.html'
  context_object_name = 'posts'
  ordering = ['-create']

  '''
  def get_context_data(self, *args, **kwargs):
    category_menu = Category.objects.all()
    context = super(HomeView, self).get_context_data(*args, **kwargs)
    context['category_menu'] = category_menu
    return context
  '''

class PostDetail(DetailView):
  model = Post
  template_name = 'theblog/post_detail.html'
  context_object_name = 'post'

  def get_context_data(self, *args, **kwargs):
    context = super(PostDetail, self).get_context_data()
    temp = get_object_or_404(Post, id=self.kwargs['pk'])

    liked = False
    if temp.likes.filter(id=self.request.user.id): #verifica se o like é do usuário logado, se sim, é pq ele já deu like
      liked = True

    total_likes = temp.total_likes()
    context['total_likes'] = total_likes
    context['liked'] = liked #com este context podemos fazer a lógica de mostrar os botões de Like e Unlike
    return context

class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  template_name = 'theblog/post_new.html'
  form_class = PostForm
  login_url = 'login'
  #fields = '__all__'
  #success_url = '/'

  #https://www.youtube.com/watch?v=TAH01Iy5AuE
  '''
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  '''

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

class CategoryCreate(LoginRequiredMixin, CreateView):
  model = Category
  template_name = 'theblog/category_new.html'
  fields = '__all__'
  success_url = reverse_lazy('home') #sem o reverse_lazy, a URL iria ficar .../category/home


#Obs: a função replace irá transformar a string em lower case, por isso se tivermos uma categoria 'Educacao Geografia',
#não irá conseguir achar esta categoria, pois ficará 'educacao geografia' e na URL, 'educacao-geografia'.
#Para isso, sobreescrevemos o método save no arquivo models.py
#Se usar o slugify do jeito que é mostrado no tutorial, teremos o problema da acentuação. No fim, não utilizei o slugify,
#assim ficará %20 nos espaços da URL.
def CategoryView(request, category):
  #category_post = Post.objects.filter(category=category.replace('-', ' '))
  #category = category.replace('-', ' ')
  category_post = Post.objects.filter(category=category)
  context = {'category': category, 'category_post': category_post}
  return render(request, 'theblog/categories.html', context)

def LikeView(request, pk):
  post = get_object_or_404(Post, id=request.POST.get('post_id'))
  liked = False
  if post.likes.filter(id=request.user.id).exists(): #já deu like
    post.likes.remove(request.user) #remove o like
    liked = False
  else:
    post.likes.add(request.user) #add like
    liked = True
  return HttpResponseRedirect(reverse('detail_post', args=[str(pk)]))

class AddCommentView(CreateView):
  model = Comment
  template_name = 'theblog/add_comment.html'
  form_class = CommentForm
  #success_url = reverse_lazy('home')

  def form_valid(self, form):
    form.instance.post_comment_id = self.kwargs['pk']
    #print(form.instance.post_comment_id)
    return super().form_valid(form)
  
  #Após o comentário, volta ao post original
  def get_success_url(self):
    return reverse_lazy('detail_post', kwargs={'pk':self.kwargs['pk']})



