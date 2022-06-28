from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from home import *
# Create your views here.

def register(request):
    
    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            return render(request, "home_page.html")


    else:
        form = UserCreationForm()
    
    
    return render(request, "register.html", {"form":form})