from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from vaults.models import Credential

from vaults.utils.encryption import decrypt
from vaults.utils.icons import get_icon_path

@method_decorator(login_required, name='dispatch')
class IndexView(View):
    def get(self, request, vault_id=None):
        user_id = request.user.id
        vaults = request.user.vaults.all().order_by('-created_at')
        user = request.user
        password_settings = user.password_settings

        print(password_settings)

        credentials = self.get_credentials(vault_id, user_id)
        
        if vault_id is None:
            newest_vault = vaults.first()
            return redirect('index', vault_id=newest_vault.id)

        try:
            vault = request.user.vaults.get(id=vault_id)
        except ObjectDoesNotExist:
            newest_vault = vaults.first()
            return redirect('index', vault_id=newest_vault.id)

        return render(request, 'index.html', {'vaults': vaults, 'user': user, 'vault': vault, 'credentials': credentials, 'password_settings': password_settings})
    
    def get_credentials(self, vault_id, user_id):
        credentials = Credential.objects.filter(vault_id=vault_id, user_id=user_id).order_by('-created_at')

        for credential in credentials:
            credential.password = decrypt(credential.password)
            credential.icon = get_icon_path(credential.url)

        return credentials
