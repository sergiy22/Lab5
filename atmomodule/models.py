from django.db import models
import uuid


class AtmoSensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text = "this is unique ID LUL")
    lon = models.FloatField()
    lat = models.FloatField()
    date = models.DateField(auto_now = True)
    time = models.TimeField(auto_now = True)
    temperature = models.FloatField()
    name = models.CharField(max_length = 100)
    model = models.CharField(max_length = 100)


class CO2Sensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text = "this is unique ID ZULUL")
    lon = models.FloatField()
    lat = models.FloatField()
    date = models.DateField(auto_now = True)
    time = models.TimeField(auto_now = True)
    pressure = models.FloatField()
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)  