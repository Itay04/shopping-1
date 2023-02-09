
from django.urls import path, include
from . import views


urlpatterns = [
    path('products/', views.products),
    path('cart/', views.cart_list), 
    path('cart/<int:pk>', views.cart_item),
]
