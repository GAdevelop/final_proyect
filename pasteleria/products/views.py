from django.shortcuts import render
from products.models import Products

# Create your views here.

def products(request):
    products = Products.objects.all()
    data = {'data' : products}

    return render(request, 'products.html', data)

def detail(request, id):
    products=Products.objects.filter(id=id)
    return render(request, 'detail.html', {'products' : products})