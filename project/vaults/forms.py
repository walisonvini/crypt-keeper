from django import forms

from .models import Credential, PasswordSettings

class CredentialForm(forms.ModelForm):
    class Meta:
        model = Credential
        fields = ['name', 'username', 'password', 'description', 'vault', 'url']

class PasswordSettingsForm(forms.ModelForm):
    class Meta:
        model = PasswordSettings
        fields = ['length', 'lowercase', 'uppercase', 'numbers', 'special_characters']