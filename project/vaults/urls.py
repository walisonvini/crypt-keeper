from django.urls import path
from . import views

urlpatterns = [
    path('vault', views.vault_view, name='vault'),
    path('vault/<int:vault_id>', views.vault_view, name='vault'),
]