from rest_framework import serializers
from .models import Product, CartItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializerTwo(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    class Meta:
        model = CartItem
        fields = ['id','quantity','product']