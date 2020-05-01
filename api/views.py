from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrdersSerializer


# Create your views here.

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'Order':'/api/order'
    }

    return Response(api_urls)

@api_view(['POST'])
def order(request):
    serializer = OrdersSerializer(data=request.data)

    if serializer.is_valid():
        print("SUNT LA SAVE")
        serializer.save()
        print("DONE")
    else:
        print("aici buba")
        print(serializer.errors)

    return Response(serializer.data)