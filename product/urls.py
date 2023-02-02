
from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.products),
    path('cart/', views.products.cart_item),
]
