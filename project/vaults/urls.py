from django.urls import path
from .views.vault import VaultView
from .views.credential import CredentialView

urlpatterns = [
    path('vault', VaultView.as_view(), name='vault'),
    path('vault/<int:vault_id>', VaultView.as_view(), name='vault'),
    path('credential', CredentialView.as_view(), name='credential'),
    path('credential/<int:id>', CredentialView.as_view(), name='credential'),
]