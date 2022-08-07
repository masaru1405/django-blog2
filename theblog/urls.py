from django.urls import path
from . import views

urlpatterns = [
  path('', views.HomeView.as_view(), name='home'),
  path('post/<int:pk>/', views.PostDetail.as_view(), name='detail_post'),
  path('new_post/', views.PostCreate.as_view(), name='new_post'),
  path('edit_post/<int:pk>/', views.PostUpdate.as_view(), name='update_post'),
  path('delete_post/<int:pk>', views.PostDelete.as_view(), name='delete_post'),
  path('new_category/', views.CategoryCreate.as_view(), name='new_category'),
  path('category/<str:category>/', views.CategoryView, name='category'),
]