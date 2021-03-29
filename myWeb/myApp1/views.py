from django.shortcuts import render
from django.http import HttpResponse                #more

# Create your views here.

class information():
    def __init__(self,name,age,country,univer):
        self.name=name
        self.age=age
        self.country=country
        self.univer=univer

def index(request):
    context={"infor":information("Ban",21,"Bac Ninh, VN","Haui")}
    return render(request=request,template_name="myApp1/index.html",context=context)     #more
