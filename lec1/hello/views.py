from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def index(render):
    return HttpResponse("Hello, World")

def malik(render):
    return HttpResponse("Hello, Malik")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
