from rest_framework import serializers
from .models import User, Product, Category, Order
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):


    re_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ( 'username', 'first_name', 'last_name', 'email','address', 'contactNumber', 'password', 're_password')
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def save(self,**kwargs):
        instance = User(username=self.validated_data['username'],
                        first_name= self.validated_data['first_name'],
                        last_name=self.validated_data['last_name'],
                        email=self.validated_data['email'],
                        address= self.validated_data['address'],
                        contactNumber = self.validated_data['contactNumber']
                        )
        password1 = self.validated_data['password']
        #print(password1)
        password2 = self.validated_data['re_password']
        if(password1 != password2):
            raise serializers.ValidationError({'password': "passwords dont match."})
        instance.set_password(password1)
        instance.save()





class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email','address', 'contactNumber')


class ProductSerializer(serializers.ModelSerializer):

    category_id = serializers.SlugRelatedField(slug_field="name", queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = ("id",
                    "name",
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



"""
class OrderSerializer(serializers.ModelSerializer):
    productlist = serializers.SlugRelatedField(slug_field="name", queryset=Product.objects.all(), many=True)


    class Meta:
        model = Order
        fields = ("total", 'productlist', 'userid')
        extra_kwargs = {'userid': {'read_only': True}}


"""



class OrderSerializer(serializers.Serializer):
    total = serializers.FloatField()
    productlist = serializers.SlugRelatedField(slug_field="name", queryset=Product.objects.all(), many=True)

    def list(self):
        userid = self.context["request"]._user.id
        instance = Order.objects.filter(userid=userid)
        print(instance)
        return instance


    def save(self, **kwargs):
        self.total = self.validated_data['total']
        #print(self.total)


        #print(self.context["request"]._user.id)
        #print(self.validated_data['productlist'])
        #self.userid = request.user.id

        userid = self.context["userid"]
        vaildated_data = {'total': self.total, 'productlist': self.validated_data['productlist'], 'userid': userid}
        return self.create(vaildated_data)

    def create(self, validated_data):
        instance = Order.objects.create(total=validated_data['total'], userid=validated_data['userid'])

        instance.productlist.set(validated_data['productlist'])

        return instance

    class Meta:
        model = Order
        fields = ("total", 'productlist', 'userid')
        read_only_fields = ('user_id',)
        #extra_kwargs = {'userid': {'read_only': True}}




