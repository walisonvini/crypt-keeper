from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

class CredentialView(View):
    def get(self, request):
        return render(request, 'vaults/credential.html')

    def post(self, request):
        return HttpResponse('Credential created')
