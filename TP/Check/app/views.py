from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from decouple import config

# Create your views here.
SECRET_KEY = config('SECRET_KEY')
size =  config('Size')

@api_view(["POST"])
def home(height):
    print(type(height))
    print(SECRET_KEY)
    print(size)
    try:
        response = {
        'id': 1,
        'name': 'Tom',
        }
        print(type(response))    
        return JsonResponse(response)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_404_BAD_REQUEST)