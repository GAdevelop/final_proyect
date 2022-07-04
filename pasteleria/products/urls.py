from django.urls import path
from . import views


urlpatterns = [
    path('', views.productList, name='products'),
    path('post/<int:id>', views.detail, name='post_detail'),
    path('addProduct', views.addProduct, name='add_product'),
    path('editProduct/<int:id>', views.editProduct, name='edit_product'),
    path('deleteProduct/<int:id>', views.deleteProduct, name='delete_product'),
    path('post/<int:id>/addComment', views.addComment, name='add_comment'),


]