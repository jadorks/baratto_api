from django.http import request
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from todo.serializers import ProductSerializer, CategorySerializer, UserSerializer
from todo.models import Products, Category
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

# Create your views here.

class ListUserAPIView(ListAPIView):
    """This endpoint lists users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(RetrieveAPIView):
    """This endpoint lists a user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CurrentUserAPIView(ListAPIView):
    """This endpoint lists the products of the logged in user"""
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id = self.request.user.id).all()

class CurrentUserProductsAPIView(ListAPIView):
    """This endpoint lists the products of the logged in user"""
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Products.objects.filter(user = self.request.user.id)

class UserProductsAPIView(ListAPIView):
    """This endpoint lists the products of a specific user"""
    serializer_class = ProductSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('pk', None)
        if user_id is not None:
            user = get_object_or_404(User, id=user_id)
            return Products.objects.filter(
                user = user
            ).all()
        else:
            return Products.objects.none()


class ListTodoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class CreateTodoAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UpdateTodoAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class DeleteTodoAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class RetrieveTodoAPIView(RetrieveAPIView):
    """This endpoint allows for retrieving a specific Todo from the database"""
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ListCategoryAPIView(ListAPIView):
    """This endpoint allows for viewing all product categories"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RetrieveCategoryAPIView(RetrieveAPIView):
    """This endpoint allows for viewing a product category"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryProductsView(ListAPIView):
    """This endpoint allows for viewing products of a specific category"""
    serializer_class = ProductSerializer

    def get_queryset(self):
        cat_id = self.kwargs.get('pk', None)
        if cat_id is not None:
            category = get_object_or_404(Category, id=cat_id)
            return Products.objects.filter(
                category = category
            ).all()
        else:
            return Products.objects.none()

