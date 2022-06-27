from django.urls import path
from . import views
from home import urls

urlpatterns = [

    path('register', views.register, name='Register')

    
]