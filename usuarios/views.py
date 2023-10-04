from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request) -> HttpResponse:
    return render(request=request, template_name='cadastro.html')
