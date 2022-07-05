from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Avatares
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
                avatares = Avatares.objects.filter(user=request.user.id)
                return render(request, 'home_page.html', {"url":avatares[0].image.url})
            
            else:
                return HttpResponse("Usuario incorrecto")
                #return render(request , "login.html",)
        else:
            #form = AuthenticationForm(initial)
            return render(request, "login.html")


    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})