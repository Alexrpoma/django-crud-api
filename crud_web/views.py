from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Address, Person


# Create your views here.
def welcome_django(request):
    return HttpResponse("<h2>Welcome to django app</h2>")


def home_page(request):
    return HttpResponse("<h2>Home Page</h2>")


def about_us(request):
    return HttpResponse("<h2>About Us</h2>")


def persons(request):
    persons_list = list(Person.objects.values())
    return JsonResponse(persons_list, safe=False)


def address(request):
    return HttpResponse('addresses')
