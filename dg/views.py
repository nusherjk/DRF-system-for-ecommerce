from django.shortcuts import render
from .models import *
from .serializers import UserSerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

class UserViwset(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=True, methods=['post'])
    def perform_create(self, request):
        #self.serializer_class(data=request.data)
        print(request.data)




class ProductViewset(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()




