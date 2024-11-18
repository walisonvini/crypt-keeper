from django.db import models
from django.conf import settings

class Vault(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vaults')

class Credential(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    vault = models.ForeignKey(Vault, on_delete=models.CASCADE, related_name='credentials')  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='credentials')

class PasswordSettings(models.Model):
    length = models.IntegerField(default=12)
    special_characters = models.BooleanField(default=True)
    numbers = models.BooleanField(default=True)
    uppercase = models.BooleanField(default=True)
    lowercase = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='password_settings')