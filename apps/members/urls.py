from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path('register', views.UserRegisterView.as_view(), name='register'),
  path('login', views.LoginInterfaceView.as_view(), name='login'),
  path('edit_settings', views.UserEditSettingsView.as_view(), name='edit_settings'),
  path('<int:pk>/profile', views.ShowProfilePageView.as_view(), name='show_profile'),
  path('<int:pk>/edit_profile_page', views.EditProfilePageView.as_view(), name='edit_profile_page'),
  path('create_profile_page/', views.CretaProfilePageView.as_view(), name='create_profile_page')
]