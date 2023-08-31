from django import forms

class PersonRegister(forms.Form):
  username = forms.CharField(label="Username", max_length=20)
  nickname = forms.CharField(label="Nickname", max_length=20)
  email = forms.CharField(label="Email", max_length=30)
  password = forms.CharField(label="Password", max_length=30)

class AddressRegister(forms.Form):
  house_number = forms.IntegerField(label="House number" , max_value=9999)
  street = forms.CharField(label="Street", max_length=15)
  city = forms.CharField(label="City", max_length=20)
  country = forms.CharField(label="Country", max_length=25)