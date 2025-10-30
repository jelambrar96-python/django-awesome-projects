from django.shortcuts import render 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework.authtoken.models import Token 

from .models import *
from .serializers import *


@api_view(['GET']) 
def get_item(request): 
    item_objs = Item.objects.all() 
    serializer = ItemSerializer(item_objs, many=True) 
    return Response({'status': 200, 'payload': serializer.data})
