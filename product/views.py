from django.shortcuts import render
# /localhost:8000/products
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CartSerializerTwo, ProductSerializer, CartSerializer
from .models import Product, CartItem



@api_view(['GET', 'POST'])
def products(request):
    """
    List all products, or create a new product.
    """
    if request.method == 'GET': # list products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': # create new product
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, pk):
#     try:
#         product = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = P(product)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = P(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         product.soft_delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def cart(request):
    if request.method == 'GET':
        cart = CartItem.objects.all()
        serializer = CartSerializerTwo(cart, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def cart_item(request, pk):
    print (request,pk)
    try:
        cart = CartItem.objects.get(pk=pk)
    except CartItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # if request.method == 'DELETE':
    #     print (request)
    #     cart=CartItem.objects.filter(product_id=pk)
    #     print (cart.value())
    #     cart.soft_delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['DELETE'])
def deletefromcart(request,pk):
    print (pk)
    if request.method == 'DELETE':
        print (request)
        cart=CartItem.objects.filter(product_id=pk)
        print (cart)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)