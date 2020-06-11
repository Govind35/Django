from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render( request, 'home.html',{'name': 'kalsa'})

def add(request):

    val1 = int(request.POST["no1"])
    val2 = int(request.POST["no2"])
    res = val1 + val2

    return render(request, 'home2.html',{'res':res})


