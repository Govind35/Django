from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Parking
from . serializers import slotseri

# Create your views here.

class slotList(APIView):
    def post(self, request, car_no):
        
        try:
            free = Parking.objects.filter(car='NA').first()
            if(free):
                free.car = car_no
                free.save()
                return Response(free.slot)
            else:
                add = Parking(car=car_no) 
                add.save()
                #serialiser = slotseri(add)
                return Response(add.slot)
        except Exception:
            return Response("Parking is full")

