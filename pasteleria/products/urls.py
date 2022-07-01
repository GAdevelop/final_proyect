from django.urls import path
#from . import views
from .views import ProductView, PostDetailView

urlpatterns = [
    path('', ProductView.as_view(), name='products'),
    path('post_detail/<int:pk>', PostDetailView.as_view(), name = 'post_detail')

]