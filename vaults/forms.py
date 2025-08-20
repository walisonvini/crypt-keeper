from django import forms
from django.conf import settings

from .models import Credential, PasswordSettings
from users.models import CustomUser

class CredentialForm(forms.ModelForm):
    class Meta:
        model = Credential
        fields = ['name', 'username', 'password', 'description', 'vault', 'url']

class PasswordSettingsForm(forms.ModelForm):
    class Meta:
        model = PasswordSettings
        fields = ['length', 'lowercase', 'uppercase', 'numbers', 'special_characters']

class AccountSettingsForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password_hint']