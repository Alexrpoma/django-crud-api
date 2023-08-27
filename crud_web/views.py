from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Address, Person
from django.shortcuts import get_object_or_404
from django.core import serializers


# Create your views here.
def welcome_django(request):
    return HttpResponse("<h2>Welcome to django app</h2>")


def home_page(request):
    return HttpResponse("<h2>Home Page</h2>")


def about_us(request):
    return HttpResponse("<h2>About Us</h2>")


def all_persons(request):
    persons_list = list(Person.objects.values())
    return JsonResponse(persons_list, safe=False)


def get_person(request, uuid):
    person = get_object_or_404(Person, id=uuid)
    person_data = {
        'id': person.id,
        'username': person.username,
        'nickname': person.nickname,
        'email': person.email
    }
    # person_serializable = serializers.serialize('json', person) --> option without mapping
    return JsonResponse(person_data, safe=False)


def address(request):
    address_list = list(Address.objects.values())
    return JsonResponse(address_list, safe=False)


# def create_persons(request):
#     person0 = Person(username='Anna', nickname='anni', email='anna@gmail.com', password='12313')
#     person1 = Person(username='Carlos', nickname='carl', email='carlos@outlook.com', password='12313')
#     person2 = Person(username='Robert', nickname='robi', email='robert@yahoo.com', password='12313')
#     Person.save(person0)
#     Person.save(person1)
#     Person.save(person2)
#     return HttpResponse('persons created!')
