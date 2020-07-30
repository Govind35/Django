from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Parking
from . serializers import slotseri


# Park the car 
class slotList(APIView):
    def post(self, request, car_no):
        try:
            if(Parking.objects.all().count() <= 50):
                freeSpace = Parking.objects.filter(car='NA').first()
                if(freeSpace):
                    freeSpace.car = car_no
                    freeSpace.save()
                    serialiser = slotseri(freeSpace)
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
                    return Response({'Error':'PARKING IS FULL 1'},status=status.HTTP_404_NOT_FOUND)
        
        except Exception:
            return Response({'Error':'PARKING IS FULL 2'},status=status.HTTP_404_NOT_FOUND)



# Remove Car
class freeSlot(APIView):
    def post(self, request, slot_no):
        try:
            found = Parking.objects.filter(slot=slot_no).first()
            found.car='NA'
            found.save()
            return Response({'Message':'Car is removed'},status=status.HTTP_200_OK)   
        
        except Exception :
            return Response({'Message':'Car is not parked/Invalid slot number'},status=status.HTTP_404_NOT_FOUND)


# Check the Car/Slot Details 
class check(APIView):
    def get(self, request,id_no):
        try:
            if(Parking.objects.filter(car=id_no)):
                carFound = Parking.objects.filter(car=id_no)
                serialiser = slotseri(carFound,many=True)
            
            elif(Parking.objects.filter(slot=id_no)):
                slotFound = Parking.objects.filter(slot=id_no)
                serialiser = slotseri(slotFound,many=True)
            
            else:
                return Response({'Message':'Invalid Credentials'},status=status.HTTP_404_NOT_FOUND)

            return Response(serialiser.data,status=status.HTTP_200_OK)
        
        except Exception :
            return Response({'Message':'Invalid Credentials'},status=status.HTTP_404_NOT_FOUND)