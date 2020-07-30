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
            if(Parking.objects.all().count() <= 10):
                freeSpace = Parking.objects.filter(car='NA').first()
                if(free):
                    freeSpace.car = car_no
                    freeSpace.save()
                    serialiser = slotseri(freeSpace)
                    return Response({'slot' : serialiser.data['slot']},status=status.HTTP_200_OK)
                else:
                    addNew = Parking(car=car_no) 
                    addNew.save()
                    serialiser = slotseri(addNew)
                    return Response({'slot' : serialiser.data['slot']},status=status.HTTP_200_OK)
            else:
                freeSpace = Parking.objects.filter(car='NA').first()
                if(freeSpace):
                    freeSpace.car = car_no
                    freeSpace.save()
                    serialiser = slotseri(freeSpace)
                    return Response({'slot' : serialiser.data['slot']},status=status.HTTP_200_OK)

                else:
                    return Response({'Error':'PARKING IS FULL'},status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'Error':'PARKING IS FULL'},status=status.HTTP_404_NOT_FOUND)




class freeSlot(APIView):
    def post(self, request, slot_no):
        
        try:
            found = Parking.objects.filter(slot=slot_no).first()
            print("1")
            found.car='NA'
            print("2")
            found.save()
            print("3")
            return Response({'Message':'Car is removed'},status=status.HTTP_200_OK)   
        except Exception :
            return Response({'Message':'Car is not parked'},status=status.HTTP_404_NOT_FOUND)

