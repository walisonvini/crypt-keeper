from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'name', 'password1', 'password2', 'password_hit')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')
    