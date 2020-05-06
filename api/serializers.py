from rest_framework import serializers
from main.models import Orders, Pizzas

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