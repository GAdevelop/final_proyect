from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from login_out.models import Avatares
# Create your views here.

def home_page(request):

    return render(request, 'home_page.html',)


@login_required
def about_us(request):
    return render(request, "about_us.html")