from django.urls import path
from . import views

urlpatterns = [
    path('viewProfile', views.viewProfile, name = 'view_profile'),
    path('editProfile', views.editProfile, name = 'edit_profile'),

]