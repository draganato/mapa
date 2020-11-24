from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Podaci
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,myForm

# Create your views here.

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    return render(request, "login.html")

def logoutUser(request):
    return redirect('login')

def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'Acount was created for '+ username)
            return redirect('login')

    return render(request, "register.html",{
        "form": form
    })

def home(request):
    if request.method == "POST":
        form = myForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['uslov']
            t = form.cleaned_data['tacka']
            p = form.cleaned_data['poligon']
            Podaci(uslov=u, tacka=t, poligon = p).save()
            return render(request, "podaci.html",{
                "title": "Pregled analiza",
                "podaci": Podaci.objects.all()
            })
        
    else:
        form=myForm()
        return render(request, "home.html",{
            "title": "Home",
            "form1": form
    })

def pregled(request):
        return render(request, "podaci.html",{
            "title": "Pregled analiza",
            "podaci": Podaci.objects.all()
        })

