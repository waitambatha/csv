from django.db import models

class ElectricVehicle(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    model_year = models.IntegerField()
    vehicle_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)


    class Meta:
        db_table = 'ElectricVehicle'