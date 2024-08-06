from django.db import models
from django.contrib.auth.models import User

class Vault(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Credential(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    vault = models.ForeignKey(Vault, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)