from django.urls import path
from .views.index import IndexView
from .views.credential import CredentialView
from .views.vault import VaultView, VaultCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:vault_id>', IndexView.as_view(), name='index'),

    path('vault', VaultView.as_view(), name='vault'),
    path('vault/create', VaultCreateView.as_view(), name='vault_create'),
    path('vault/<int:vault_id>', VaultView.as_view(), name='vault_edit'),

    path('credential', CredentialView.as_view(), name='credential'),
    path('credential/<int:id>', CredentialView.as_view(), name='credential'),
]