from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from todo.serializers import UsersSerializer
from todo.models import Users
from todo.serializers import ProductsSerializer
from todo.models import Products


# Create your views here.
class ListUsersAPIView(ListAPIView):
    """This endpoint list all of the available users from the database"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class ListProductsAPIView(ListAPIView):
    """This endpoint list all of the available products from the database"""
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer    

class CreateUsersAPIView(CreateAPIView):
    """This endpoint allows for creation of a User"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class CreateProductsAPIView(CreateAPIView):
    """This endpoint allows for creation of a Product"""
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    
class UpdateUsersAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific User by passing in the id of the todo to update"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    
class UpdateProductsAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Product by passing in the id of the todo to update"""
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer    


class DeleteUsersAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Users from the database"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    
 class DeleteProductsAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Product from the database"""
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    
# Users viewset
class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    
# Products viewset
class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'Name']
    search_fields = ['=Name', 'Description']
    ordering_fields = ['Name', 'id']
    ordering = ['id']
    
