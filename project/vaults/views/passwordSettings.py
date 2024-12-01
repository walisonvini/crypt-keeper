from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect

from vaults.models import PasswordSettings
from vaults.forms import PasswordSettingsForm

@method_decorator(login_required, name='dispatch')
class PasswordSettingsView(View):
    def get(self, request):
        password_settings = PasswordSettings.objects.get(user=request.user)
        form = PasswordSettingsForm(instance=password_settings)
        vaults = request.user.vaults.all()
        return render(request, 'password_settings.html', {'password_settings': password_settings, 'form': form, 'vaults': vaults})

    def post(self, request):
        password_settings = PasswordSettings.objects.get(user=request.user)
        form = PasswordSettingsForm(request.POST, instance=password_settings)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password settings updated successfully.')
            return redirect('password_settings')
        vaults = request.user.vaults.all()
        return render(request, 'password_settings.html', {'password_settings': password_settings, 'vaults': vaults})