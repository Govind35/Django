from django.db import models

# Create your models here.

class Parking(models.Model):
    slot = models.AutoField(primary_key=True)
    car = models.CharField(max_length=10)
    
    def __str__(self): 
        return self.car   
