from django.shortcuts import render
from django.http import HttpResponse #more

# Create your views here.
def index(request):
    return HttpResponse("hello Django")
def app1(request):
    return HttpResponse("This's an app1")
