from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    password_hint = models.CharField(max_length=150, blank=True, null=True)

    first_name = None 
    last_name = None
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
