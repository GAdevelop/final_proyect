from dataclasses import fields
from django import forms
from products.models import Products, Comments



class ProductForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ['title', 'subtitle', 'image', 'body']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['title', 'body']

