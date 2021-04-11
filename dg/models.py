from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
# Create your models here.


class User(AbstractUser):
    address = models.CharField(max_length=2000)
    contactNumber = models.CharField(max_length=15)


# Products models
class Category(models.Model):
    id = models.UUIDField(auto_created=True, default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=300)

class Product(models.Model):
    id = models.UUIDField(auto_created=True, default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=300)
    price = models.FloatField()
    images = models.ImageField(null=True)
    #brand
    description = models.CharField(max_length=2500)
    size = models.CharField(max_length=20) # Probable JSON field
    #colors
    availability = models.BooleanField()
    category_id = models.ForeignKey(Category, related_name='cat_id', on_delete=models.CASCADE)# ManytoManyfields because of some product might have multiple category
    details = models.CharField(max_length=2500)


class ProductReview(models.Model):
    id = models.UUIDField(auto_created=True, default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=300)
    email = models.EmailField()
    review = models.CharField(max_length=3000)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    id = models.UUIDField(auto_created=True, default=uuid4, primary_key=True, unique=True)
    #name = models.CharField(max_length=300)
    #email = models.EmailField()
    #address = models.CharField(max_length=2000)
    total = models.FloatField(null=True)
    productlist = models.ManyToManyField(Product)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)

