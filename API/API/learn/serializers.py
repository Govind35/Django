from rest_framework import serializers
from . models import employee, Parking

class employeeseri(serializers.ModelSerializer):

    class Meta:
        model = Parking
#        fields = ('firstname','lastname')   for specific value to return
        fields = ('slot')    #'__all__' 
        