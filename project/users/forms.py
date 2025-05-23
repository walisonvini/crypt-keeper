from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .validators import validate_password_hint

class RegisterForm(UserCreationForm):
    password_hint = forms.CharField(required=False)

    class Meta:
        model = get_user_model()
        fields = ('email', 'name', 'password1', 'password2', 'password_hint')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password_hint = cleaned_data.get("password_hint")

        if password1 and password_hint:
            try:
                validate_password_hint(password1, password_hint)
            except ValidationError as e:
                self.add_error('password_hint', e)  # Add error to the specific field

        return cleaned_data

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')
    