from django import forms

from .models import Vault, Credential

class VaultForm(forms.ModelForm):
    class Meta:
        model = Vault
        fields = ['name']

class CredentialForm(forms.ModelForm):
    class Meta:
        model = Credential
        fields = ['name', 'username', 'password', 'description', 'url', 'vault', 'user']

    