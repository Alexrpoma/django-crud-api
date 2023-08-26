from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome_django(request):
    return HttpResponse("<h2>Welcome to django app</h2>")
