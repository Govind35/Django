from rest_framework import serializers
from . models import Parking

class slotseri(serializers.ModelSerializer):

    class Meta:
        model = Parking
        fields = '__all__' 
        