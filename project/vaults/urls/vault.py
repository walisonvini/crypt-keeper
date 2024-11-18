from django.urls import path
from ..views.vault import VaultView, VaultCreateView

app_name = 'vault'

urlpatterns = [
    path('', VaultView.as_view(), name='list'),
    path('create/', VaultCreateView.as_view(), name='create'),
    path('<int:vault_id>/', VaultView.as_view(), name='edit'),
    path('<int:vault_id>/delete/', VaultView.as_view(), name='delete')
]
