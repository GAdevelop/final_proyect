from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
# Create your views here.

def register(request):
    
    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            return render(request, "home/home_page.html")


    else:
        form = UserCreationForm()
    
    
    return render(request, "register.html", {"form":form})