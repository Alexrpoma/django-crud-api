from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from crud_web.register import PersonRegister, AddressRegister
from .models import Address, Person
from django.shortcuts import get_object_or_404
from django.core import serializers


# Create your views here.
def home_page(request):
    message = 'This is the best django course!!'
    return render(request, 'index.html', {
        'message': message
    })


def about_us(request):
    return render(request, 'about.html')


def all_persons(request):
    person_obj = Person.objects.all()
    return render(request, 'person.html', {
        'persons': person_obj
    })


def get_person(request, uuid):
    person = get_object_or_404(Person, id=uuid)
    address = get_object_or_404(Address, id=person.address.id)
    address_data = {
        'id': address.id,
        'house_number': address.house_number,
        'street': address.street,
        'city': address.city,
        'country': address.country
    }
    person_data = {
        'id': person.id,
        'username': person.username,
        'nickname': person.nickname,
        'email': person.email,
        'address': address_data
    }
    # person_serializable = serializers.serialize('json', person) --> option without mapping
    return JsonResponse(person_data, safe=False)


def get_address(request, uuid):
    address = get_object_or_404(Address, id=uuid)
    address_data = {
        'id': address.id,
        'house_number': address.house_number,
        'street': address.street,
        'city': address.city,
        'country': address.country
    }
    return JsonResponse(address_data, safe=False)


def address(request):
    address_list = list(Address.objects.values())
    address_objs = Address.objects.all()
    return render(request, 'address.html', {
        'address_str': address_list,
        'address_objs': address_objs
    })

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {
            'person_register': PersonRegister,
            'address_register': AddressRegister
        })
    elif request.method == 'POST':
        print(request.POST)
        person_address = Address.objects.create(
            house_number=request.POST['house_number'],
            street=request.POST['street'],
            city=request.POST['city'],
            country=request.POST['country']
        )
        Person.objects.create(
            username=request.POST['username'],
            nickname=request.POST['nickname'],
            email=request.POST['email'],
            password=request.POST['password'],
            address=person_address
            )
        return redirect('/person')



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