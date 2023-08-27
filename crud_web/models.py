from django.db import models
import uuid


# Create your models here.
class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    username = models.CharField(max_length=10)
    nickname = models.CharField(max_length=10)
    email = models.CharField(max_length=20,  unique=True)
    password = models.CharField(max_length=20)


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    house_number = models.IntegerField(unique=True)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

