from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class myForm(forms.Form):
    uslov = forms.BooleanField(required=False)
    tacka = forms.CharField(max_length=200)
    poligon = forms.CharField(max_length=400)

