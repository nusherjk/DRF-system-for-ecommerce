from rest_framework import serializers
from .models import User, Product, Category


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    """
    id = models.UUIDField(auto_created=True, default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=300)
    price = models.FloatField()
    images = models.ImageField()
    #brand
    description = models.CharField(max_length=2500)
    size = models.CharField(max_length=20) # Probable JSON field
    #colors
    availability = models.BooleanField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)# ManytoManyfields because of some product might have multiple category
    details = models.CharField(max_length=2500)
    """





    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model= Category
        fields = ('name',)


