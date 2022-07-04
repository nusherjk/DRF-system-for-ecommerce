from django.shortcuts import render
from .models import *
from .serializers import UserSerializer, ProductSerializer, CategorySerializer, OrderSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet,ViewSet, ReadOnlyModelViewSet
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsProviderOrReadOnly, IsSelforAdmin
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
# Create your views here.



def index(request):
    return HttpResponse("<h1>This Api is working</h1>")


class Home(TemplateView):

    template_name = "home.html"



class UserViwset(ModelViewSet):

    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()


    """
    def get_permissions(self):
        if self.action == 'list' or self.action == 'create':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsSelforAdmin]

        return [permission() for permission in permission_classes]
    """

    @action(detail=True, methods=['post'])
    def perform_create(self, request):
        print(self.request.data)
        data =self.serializer_class(data=self.request.data)
        if(data.is_valid()):
            data.save()
            return Response({"status": HTTP_200_OK, "data": data})
        else:
            print(data.errors)
            print("Form Data is not valid")



class ProfileViewset(ReadOnlyModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = User.objects.all()


    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAdminUser]

        elif(self.action == 'retrieve'):
            # permission_classes= [IsSelforAdmin]
            permission_classes = [IsAuthenticated]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
    

    # TODO: Retrive data of the subject (Work Left!!!)
    def retrieve(self, request, pk=None, *args, **kwargs):
        # query = self.queryset.get(pk=pk)
        # print(query.id)
        sd=self.serializer_class(instance=self.request.user)
        # if sd.is_valid():
        return Response({"status": HTTP_200_OK, "data": sd.data})


class ProductViewset(ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    """
    def get_permissions(self):
        if(self.action=='list' or self.action== 'retrieve'):
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
            
        return [permission() for permission in permission_classes]

    """
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
# TODO: Providers can only select categories not create categories
class CategoryViwset(ModelViewSet):
    permission_classes = [IsProviderOrReadOnly]
    # permission_classes = [IsAdminUser]
    authentication_classes = (TokenAuthentication,) 
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs):
        data = self.queryset
        serializer = serializers.serialize('json', data)
        return Response(serializer)

    @action(detail=True, methods=['post'])
    def perform_create(self, request):


        data =self.serializer_class(data=request.data)
        if(data.is_valid()):
            data.save()
            return Response({"status": HTTP_200_OK, "data": data})
        else:
            return Response("Form Data is not valid")


class Orderviewset(ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        instance = Order.objects.filter(userid=self.request.user.id)
        return instance

    def perform_create(self, request):
        data = self.request.data

        #userid = request.context.get("request").user
        #data["userid"] = userid.id

        #print(self.serializer_class.context("request").user.id)
        #data['userid'] = request.user
        oserializer = OrderSerializer(data=data, context={'userid': self.request.user})

        if(oserializer.is_valid()):
            oserializer.save()
            return Response(oserializer.data)
        else:
            print(oserializer.errors)

class Webhookviewset(APIView):
    permission_classes = [AllowAny]
    verify_token = "EAAEY6GWtTxUBABrrpNTHRf6lX8gnGRyxt3iZBWp9Do24WE6cnZCcCIgvO44OjsQZAzsSRV8ioT89mitN4wroZCwlAwLJPJZBpOkvcjJaRr2EcJcMMLBecOkWimtES3cUKXy9KZAaiBZAkHtKxAJvIyagYZC6UIDLhmUrwgDFhVKXB7Gkfv74Y6FEnvynBIyAIJUMrRgRsw5L7QZDZD"

    def get(self, request):
        '''

        :param request:
        :return:
        '''
        #print(request.GET.get())
        mode = request.GET.get('hub.mode')
        token = request.GET.get('hub.verify_token')
        challenge = request.GET.get('hub.challenge')

        if (mode and token):
            if(mode== 'subscribe' and token == self.verify_token):
                print("Webhook Verified")
                return Response({"status": HTTP_200_OK, "data":challenge })
            else:
                return Response({"status": HTTP_403_FORBIDDEN})
        else:
            return Response({'status': HTTP_404_NOT_FOUND})

    def post(self, request):
        '''

        :param request:
        :return:
        '''



        body = request.body

        if (body.object == 'page'):
            for entry in body.entry:
                webhook_event = entry.messaging[0]
                print(webhook_event)
            return Response("EVENT_RECEIVED")
        else:
            return Response({"status": HTTP_404_NOT_FOUND})

    @classmethod
    def get_extra_actions(cls):
        return []