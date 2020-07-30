from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employee, Parking
from . serializers import employeeseri


# Create your views here.


class employeeList(APIView):

    def get(self,request):
        if(request.method == "GET"):
            #employee1 = Parking(car='NA')
            #mployee1.save()

            employee2 = Parking.objects.get(car='NA')
            #employee1.car = 'MH123456'
            serialiser = employeeseri(employee2, many=True)
            return Response(serialiser)
        else:
            return Response("NO RESPONSE")     
    
    def post(self, request):

        print("POST")
        return Response("POST")     

        

