from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, RedirectView
from django.urls import reverse_lazy

from .forms import LoginForm, RegisterForm
from vaults.models import Vault, PasswordSettings

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'auth/login.html'

    def form_valid(self, form):
        return super().form_valid(form)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()

        self.create_vault(user)
        self.create_password_settings(user)

        return super().form_valid(form)

    def create_vault(self, user):
        vault = Vault(name='My Vault', user=user)
        vault.save()

    def create_password_settings(self, user):
        password_settings = PasswordSettings(user=user)
        password_settings.save()

class LogoutView(RedirectView):
    url = reverse_lazy('login')
    permanent = False
    query_string = True
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        self.request.session.flush()
        return super().get_redirect_url(*args, **kwargs)
