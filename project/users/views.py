from django.contrib.auth.views import LoginView
from django.views import generic
from django.urls import reverse_lazy

from .forms import LoginForm, RegisterForm
from vaults.models import Vault

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'auth/login.html'

    def form_valid(self, form):
        return super().form_valid(form)


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()

        self.create_vault(user)

        return super().form_valid(form)

    def create_vault(self, user):
        vault = Vault(name='My Vault', user=user)
        vault.save()
