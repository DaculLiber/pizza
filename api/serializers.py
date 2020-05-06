from rest_framework import serializers
from main.models import Orders, Pizzas
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id']

class PizzasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizzas
        fields = ['name', 'description', 'price']


class OrdersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Orders
        fields = ["user", "price", "address", "content"]


'''

{
    "user": [
        {
            "id": "2"
        }
    ],
    "content": [ 
         {
            "name":"Margheritta"
          }
     ],
    "price": "15",
    "address": "test"
}

'''