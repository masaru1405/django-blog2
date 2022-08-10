from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path('register', views.UserRegisterView.as_view(), name='register'),
  path('edit_profile', views.UserEditView.as_view(), name='edit_profile'),

  path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html')),
  path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html')),
  path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html')),
  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html')),
  path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
  path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html')),
]