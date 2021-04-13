from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from todo.serializers import UsersSerializer
from todo.models import Users

# Create your views here.
class ListUsersAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class CreateUsersAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UpdateUsersAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class DeleteUsersAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Users from the database"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
