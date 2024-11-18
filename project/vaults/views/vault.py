from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import CreateView
from django.shortcuts import render, redirect

from vaults.models import Vault
from vaults.forms import VaultForm

@method_decorator(login_required, name='dispatch')
class VaultView(View):
    def get(self, request):
        vaults = request.user.vaults.all().order_by('-created_at')

        return render(request, 'vault/index.html', {'vaults': vaults})

@method_decorator(login_required, name='dispatch')
class VaultCreateView(CreateView):
    model = Vault
    form_class = VaultForm
    template_name = 'vault/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return redirect('vault')