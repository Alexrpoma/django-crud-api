from django.db import models
from uuid import uuid4


# Create your models here.
class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    house_number = models.IntegerField(unique=True)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return (f'(id={self.id} '
                f'house_number={self.house_number} '
                f'street={self.street} '
                f'city={self.city} '
                f'country={self.country} '
                f'person_id={self.person})')
    

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=10)
    nickname = models.CharField(max_length=10)
    email = models.CharField(max_length=20,  unique=True)
    password = models.CharField(max_length=20)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f'(id={self.id} username={self.username} nickname={self.nickname} email={self.email})'


