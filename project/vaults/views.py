from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from .models import Vault

@login_required
def vault_view(request, vault_id=None):
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