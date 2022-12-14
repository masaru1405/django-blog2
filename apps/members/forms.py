from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms
from theblog.models import Profile

class LoginForm(AuthenticationForm):
   username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Username'}))
   password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'}))

class SignUpForm(UserCreationForm):
   username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
   password1 = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
   password2 = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Confirmation'}))
   email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
   first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
   last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

   class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
   
   #para os campos username, password1 e password2, temos que fazer dessa forma para add uma classe caso não coloquemos os atributos acima
   """ def __init__(self, *args, **kwargs):
      super(SignUpForm, self).__init__(*args, **kwargs)
      self.fields['username'].widget.attrs['class'] = 'form-control'
      self.fields['password1'].widget.attrs['class'] = 'form-control'
      self.fields['password2'].widget.attrs['class'] = 'form-control' """
   
   def clean_email(self):
      email = self.cleaned_data['email']
      if User.objects.filter(email=email).exists():
         raise ValidationError('An user with this email already exists.')
      return email

class EditProfileForm(UserChangeForm):
   email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
   first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
   last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
   username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
   #last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
   #is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
   #is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
   #is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
   #date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

   class Meta:
      model = User
      #fields = ['username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined']
      fields = ['username', 'first_name', 'last_name', 'email']

class CreateProfileForm(forms.ModelForm):
   class Meta:
      model = Profile
      exclude = ['user']
      widgets = {
         'bio': forms.Textarea(attrs={'class': 'form-control'}),
         #'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
         'website_url': forms.TextInput(attrs={'class': 'form-control'}),
         'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
         'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
         'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
         'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
         'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),
      }