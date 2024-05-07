from django.db import models

class Farmer(models.Model):
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

class Farm(models.Model):
    region = models.CharField(max_length=100)
    culture = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

class AgriculturalZone(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

class Sensor(models.Model):
    type = models.CharField(max_length=100)
    measure = models.DecimalField(max_digits=9, decimal_places=2)
    zone_number = models.IntegerField()

class Valve(models.Model):
    state = models.BooleanField()
    battery_lvl = models.DecimalField(max_digits=5, decimal_places=2)
    numero_zone = models.IntegerField()

class Resource(models.Model):
    state = models.CharField(max_length=100)
    electricity_state = models.CharField(max_length=100)
    hardware_state = models.CharField(max_length=100)

class Schedule(models.Model):
    numdays = models.CharField(max_length=100)
    open_date = models.DateTimeField()
    close_date = models.DateTimeField()

class Pump(models.Model):
    number_pumps = models.IntegerField()

class Well(models.Model):
    number_wells = models.IntegerField()

class Maps(models.Model):
    localization_zones = models.CharField(max_length=100)
    localization_farm = models.CharField(max_length=100)

class Alarm(models.Model):
    state = models.BooleanField()

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profiles/')
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

class Notification(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
class File(models.Model):
    name = models.CharField(max_length=255)
    date_import = models.DateTimeField(auto_now_add=True)
    etat = models.CharField(max_length=20, choices=[('treated', 'Treated'), ('not_treated', 'Not Treated')])
    taille = models.IntegerField() 