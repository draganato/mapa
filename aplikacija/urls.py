from django.urls import path
from . import views

urlpatterns = [
    path("", views.loginPage, name="login"),
    path("home/", views.home, name= "home"),
    path("pregled/", views.pregled, name="pregled"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerPage, name="register")
]