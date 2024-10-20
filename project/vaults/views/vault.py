from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from vaults.models import Vault
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist


@method_decorator(login_required, name='dispatch')
class VaultView(View):
    def get(self, request, vault_id=None):
        user_id = request.user.id
        vaults = Vault.objects.filter(user_id=user_id).order_by('-created_at')
        user = request.user
        
        if vault_id is None:
            newest_vault = vaults.first()
            return redirect('vault', vault_id=newest_vault.id)

        try:
            vault = Vault.objects.get(id=vault_id, user_id=user_id)
        except ObjectDoesNotExist:
            newest_vault = vaults.first()
            return redirect('vault', vault_id=newest_vault.id)

        return render(request, 'vault.html', {'vaults': vaults, 'user': user, 'vault': vault})

    def post(self, request):
        return HttpResponse('Vault created')