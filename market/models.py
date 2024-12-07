from django.contrib.postgres.fields import ArrayField
from django.db import models
import uuid

class Vehicle(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    model = models.CharField(blank=False, null=False, max_length=30)
    gear_uuid = models.ManyToManyField("Gear", through='VehicleGear')
    
class Manufacturer(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(blank=False, null=False, max_length=30)
        
class Gear(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(blank=False, null=False, max_length=120)
    image = models.FileField(upload_to="media")

class VehicleGear(models.Model):
    gear_uuid = models.ForeignKey(Gear, on_delete=models.CASCADE)
    vehicle_uuid = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    years = models.CharField(blank=False, null=False, max_length=120)
    
    class Meta:
        unique_together = ('gear_uuid', 'vehicle_uuid')

class GearCategories(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    gear_uuid = models.ForeignKey(Gear, on_delete=models.CASCADE)
    name = models.CharField(blank=False, null=False, max_length=120)
        
class Codes(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    gear_uuid = models.ForeignKey(Gear, on_delete=models.CASCADE)
    name = models.CharField(blank=False, null=False, max_length=60)
    code_type = models.CharField(default="manufacturer",blank=False, null=False, max_length=40)
    