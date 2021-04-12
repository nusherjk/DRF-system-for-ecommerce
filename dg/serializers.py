from rest_framework import serializers
from .models import User, Product, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name",
                  "price",
                  'images',
                  'description',
                  'size',
                  'availability',
                  'category_id',
                  'details')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = ('name',)


