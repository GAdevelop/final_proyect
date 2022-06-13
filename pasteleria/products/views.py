from django.shortcuts import render
from products.models import Products

# Create your views here.

def products(request):
    products = Products.objects.all()
    data = {'data' : products}

    return render(request, 'products.html', data)