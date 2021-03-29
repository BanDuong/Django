from django.shortcuts import render
from .models import Question

# Create your views here.
def base(request):
    return render(request=request,template_name="myApp1/base.html")

def index(request):
    context={"name":"Ban Duong","age":21}
    return render(request=request,template_name="myApp1/index.html",context=context)     #more

def questions_list(request):
    ques_list = Question.objects.all()
    context = {"questions" : ques_list}
    return render(request=request,template_name="myApp1/questions_list.html",context=context)

