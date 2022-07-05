from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from products.models import Products, Comments
from django.contrib.auth.decorators import login_required
from products.forms import ProductForm, CommentForm
from datetime import datetime




# Create your views here.

def productList(request):
    products = Products.objects.all()

    return render(request, 'products.html', {'products': products})



def detail(request, id):
    products = Products.objects.filter(id=id)

    return render(request, 'detail.html', {'products': products})




@login_required
def addProduct(request):
    if request.method == 'POST':

        my_form = ProductForm(request.POST, request.FILES)
        if my_form.is_valid():

            post = my_form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('products')

        return render(request, 'addProduct.html', {'my_form': my_form})
    return render(request, 'addProduct.html')




@login_required
def editProduct(request, id):
    product = get_object_or_404(Products, id=id)
    if request.method == 'POST':

        my_form = ProductForm(request.POST, request.FILES, instance=product)
        if my_form.is_valid():

            product = my_form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('products')
    else:
        my_form = ProductForm(instance=product)
    return render(request, 'editProduct.html', {'my_form': my_form})



@login_required
def deleteProduct(request, id):
    product = Products.objects.filter(id=id)
    product.delete()

    return redirect('products')




@login_required
def addComment(request, id):
    products = get_object_or_404(Products, id=id)

    #my_form = CommentForm(instance=products)
    if request.method == 'POST':
        my_form = CommentForm(request.POST)

        if my_form.is_valid():
    
            comment = my_form.save(commit=False)
            comment.author = request.user
            comment.post = products
            comment.save()
            return redirect('post_detail', id=products.id)
        else:
            return HttpResponse(f'mal')
    else:
        my_form = CommentForm()

    return render(request, 'addComment.html', {'my_form': my_form})



