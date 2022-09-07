from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request, s):
    return HttpResponse(f'Hello {s} World!!!')
