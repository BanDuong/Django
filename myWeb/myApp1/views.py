from django.shortcuts import render
from django.http import HttpResponse #more

# Create your views here.

def index(request):
    return HttpResponse("hello")
