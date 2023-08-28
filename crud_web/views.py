from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Address, Person
from django.shortcuts import get_object_or_404
from django.core import serializers


# Create your views here.
def home_page(request):
    return HttpResponse("<h1>Welcome to Django!</h1>")


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


def default_data(request):

    person0 = Person(username='Anna', nickname='annie', email='anna@gmail.com', password='12313')
    person1 = Person(username='Carlos', nickname='carl', email='carlos@outlook.com', password='12313')
    person2 = Person(username='Robert', nickname='robin', email='robert@yahoo.com', password='12313')

    address0 = Address(house_number=133, street='Alamos', city='La Paz', country='Bolivia', person=person0)
    address1 = Address(house_number=562, street='Rios', city='Quito', country='Ecuador', person=person1)
    address2 = Address(house_number=485, street='Mercedes', city='Bogota', country='Colombia', person=person2)

    Person.objects.bulk_create([person0, person1, person2])
    Address.objects.bulk_create([address0, address1, address2])

    return HttpResponse('persons created!')












# A way to create persons objects:
""" person_data = [
         {'username':'Anna', 'nickname':'annie', 'email':'anna@gmail.com', 'password':'12313'},
         {'username':'Carlos', 'nickname':'carl', 'email':'carlos@outlook.com', 'password':'12313'},
         {'username':'Robert', 'nickname':'robin', 'email':'robert@yahoo.com', 'password':'12313'}
     ]
     for list_person in person_data:
         Person.objects.create(**list_person) """