from django.shortcuts import render
from products.models import Products
from django.views.generic import ListView, DetailView


# Create your views here.

class ProductView(ListView):
    model = Products
    template_name = 'products.html'

class PostDetailView(DetailView):
    model = Products
    template_name = 'detail.html'

