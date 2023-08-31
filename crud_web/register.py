from django import forms

class Register(forms.Form):
  username = forms.CharField(label="Username", max_length=20)
  nickname = forms.CharField(label="Nickname", max_length=20)
  email = forms.CharField(label="Email", max_length=30)
  password = forms.CharField(label="Password", max_length=30)