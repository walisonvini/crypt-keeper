from django.urls import path, include
from .views.index import IndexView
from .views.credential import CredentialView
from .views.vault import VaultListView, VaultCreateView, VaultUpdateView, VaultDeleteView
from .views.passwordSettings import PasswordSettingsView
from .views.accountSettings import AccountSettingsView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:vault_id>', IndexView.as_view(), name='index'),

    path('vault', VaultListView.as_view(), name='vault_list'),
    path('vault/create', VaultCreateView.as_view(), name='vault_create'),
    path('vault/<int:pk>/edit', VaultUpdateView.as_view(), name='vault_edit'),
    path('vault/<int:pk>/delete', VaultDeleteView.as_view(), name='vault_delete'),

    path('credential', CredentialView.as_view(), name='credential'),
    path('credential/<int:id>', CredentialView.as_view(), name='credential'),

    path('passowrd-settings', PasswordSettingsView.as_view(), name='password_settings'),
    path('account-settings', AccountSettingsView.as_view(), name='account_settings'),
]