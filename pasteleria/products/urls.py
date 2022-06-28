from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('detail/<int:id>', views.detail, name= 'detail'),

]