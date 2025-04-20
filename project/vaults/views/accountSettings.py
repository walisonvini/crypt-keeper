
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect

from vaults.forms import AccountSettingsForm

@method_decorator(login_required, name='dispatch')
class AccountSettingsView(View):
    def get(self, request):
        form = AccountSettingsForm(instance=request.user)
        vaults = request.user.vaults.all()
        return render(request, 'account_settings.html', {'form': form, 'vaults': vaults})

    def post(self, request):
        form = AccountSettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account settings updated successfully.')
            return redirect('account_settings')
        return render(request, 'account_settings.html', {'form': form})