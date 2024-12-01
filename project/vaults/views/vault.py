from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from vaults.models import Vault

@method_decorator(login_required, name='dispatch')
class VaultListView(ListView):
    model = Vault
    template_name = 'vault/index.html'
    context_object_name = 'vaults'
    ordering = ['-created_at']

    def get_queryset(self):
        return Vault.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class VaultCreateView(CreateView):
    model = Vault
    fields = ['name']
    template_name = 'vault/create.html'
    success_url = reverse_lazy('vault_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vaults'] = Vault.objects.filter(user=self.request.user)

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        messages.success(self.request, "Vault created successfully!")

        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class VaultUpdateView(UpdateView):
    model = Vault
    fields = ['name']
    template_name = 'vault/update.html'
    success_url = reverse_lazy('vault_list')
    context_object_name = 'vault'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vaults'] = Vault.objects.filter(user=self.request.user)

        return context

    def form_valid(self, form):
        messages.success(self.request, "Vault updated successfully!")

        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class VaultDeleteView(DeleteView):
    model = Vault
    template_name = 'vault/delete.html'
    success_url = reverse_lazy('vault_list')
    context_object_name = 'vault'

    success_message = "Vault deleted successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vaults'] = Vault.objects.filter(user=self.request.user)

        return context

    def delete(self, request, *args, **kwargs):

        return super().delete(request, *args, **kwargs)