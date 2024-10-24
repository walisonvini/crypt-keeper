import json
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import JsonResponse

from vaults.models import Credential
from vaults.forms import CredentialForm
from ..utils.encryption import encrypt

@method_decorator(login_required, name='dispatch')
class CredentialView(View):
    http_method_names = ['get', 'post', 'put', 'delete']

    def post(self, request):
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
        
    def put(self, request, id):
        try:
            credential = request.user.credentials.get(id=id)
        except Credential.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'credential not found'}, status=404)
        
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        
        form = CredentialForm(data, instance=credential)
        if form.is_valid():
            credential.name = form.cleaned_data['name']
            credential.username = form.cleaned_data['username']
            credential.password = encrypt(form.cleaned_data['password'])
            credential.description = form.cleaned_data['description']

            credential.save()

            return JsonResponse({'status': 'success', 'message': 'credential updated successfully'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
        
    def delete(self, request, id):
        try:
            credential = request.user.credentials.get(id=id)
        except Credential.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'credential not found'}, status=404)
        
        credential.delete()

        return JsonResponse({'status': 'success', 'message': 'credential deleted successfully'}, status=200)
