from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from home import urls


urlpatterns = [

    path('login', views.login_request, name='Login'),
    path('logout' , LogoutView.as_view(template_name="home_page.html"), name='Logout')
    
]