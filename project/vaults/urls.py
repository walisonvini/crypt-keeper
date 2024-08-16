from django.urls import path
from . import views

urlpatterns = [
    path('', views.vault_view, name='vault'),
]