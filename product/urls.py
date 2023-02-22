
from django.urls import path, include
from . import views

app_name='product'

urlpatterns = [
    path('products/', views.products),
    path('cart/', views.cart), 
    path('cart/<int:pk>', views.cart_item),
    path('deletefromcart/<pk>',views.deletefromcart,name='deletefromcart')
]
