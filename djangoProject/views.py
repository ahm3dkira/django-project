from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the index page.")

def about(request):
    return HttpResponse("Hello, world. You're at the about page.")

