from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_world(req):
    return HttpResponse("Hello World!")

def sample(req):
    return HttpResponse(":)")

def test(req):
    return HttpResponse("It worked!")

def create_collection(req):
    return HttpResponse("Collection is created!")
