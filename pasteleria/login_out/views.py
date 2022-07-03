from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from home import *
# Create your views here.

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request , "home_page.html", {"mensaje": f'Bienvenido {username}'})
            
            else:
                return render(request , "home_page.html", {"mensaje": "Error, datos incorrectos."})
        else:
            #form = AuthenticationForm(initial)
            return render(request, "login.html")


    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})