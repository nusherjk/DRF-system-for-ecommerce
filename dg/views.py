from django.shortcuts import render
from .models import *
from .serializers import UserSerializer, ProductSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
# Create your views here.



def index(request):
    return HttpResponse("<h1>This Api is working</h1>")


class UserViwset(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=True, methods=['post'])
    def perform_create(self, request):
        data =self.serializer_class(data=request.data)
        if(data.is_valid()):
            data.save()
            return Response({"status": HTTP_200_OK, "data": data})
        else:
            return Response("Form Data is not valid")




class ProductViewset(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()




    @action(detail=True, methods=['post'])
    def perform_create(self, request):
        data = request.data
        print(data)
        #category = get_object_or_404(Category, id=data['category_id'])
        #data['category_id']= category
        print(data)




        serializer = self.serializer_class(data=data)
        

        if(serializer.is_valid()):
            serializer.save(images = self.request.data.get('images'))
            return Response({"status": HTTP_200_OK, "data": data})
        else:
            print( serializer.errors)




"""
class Productget(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    def get_queryset(self):
        return Product.objects.all()

    def list(self, request, pk= None, **kwargs):
        data= self.get_queryset()
        serilizer = serializers.serialize('json', data)
        return Response(serilizer)
"""

class CategoryViwset(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs):

        return self.queryset

    @action(detail=True, methods=['post'])
    def perform_create(self, request):


        data =self.serializer_class(data=request.data)
        if(data.is_valid()):
            data.save()
            return Response({"status": HTTP_200_OK, "data": data})
        else:
            return Response("Form Data is not valid")


