from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import JsonResponse

from vaults.forms import CredentialForm
from ..utils.encryption import encrypt

@method_decorator(login_required, name='dispatch')
class CredentialView(View):

    def post(self, request):
        print(request.POST)
        form = CredentialForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.password = encrypt(form.instance.password)

            ## If the description is empty, set it to None
            if form.instance.description == '':
                form.instance.description = None

            form.save()

            return JsonResponse({'status': 'success', 'message': 'credential created successfully'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
