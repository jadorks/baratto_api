from rest_framework import serializers
from django.contrib.auth.models import User
from todo.models import Products, Category


class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'products', 'email']

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Products
        fields = "__all__"

    def to_representation(self, instance):
        rep = super(ProductSerializer, self).to_representation(instance)
        print(rep["category"])
        rep['category'] = instance.category.title
        return rep

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
