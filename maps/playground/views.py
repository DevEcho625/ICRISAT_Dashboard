from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def caclulate():
    x =1
    y =1
    return x+y

def hello(request):
    x = caclulate()
    y=1 
    return render(request, "hello.html", {"name": "Mosh"})
