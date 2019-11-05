from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tmpview(request):
    print(request.body)
    return HttpResponse(status=200)
