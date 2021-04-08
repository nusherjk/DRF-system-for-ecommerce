from django.shortcuts import render
from .models import *
from .serializers import UserSerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

class UserViwset(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=True, methods=['put'])
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
        serializer = self.serializer_class(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"status": HTTP_200_OK, "data": data})




