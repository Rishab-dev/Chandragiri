from django.db import models

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=250)
    eventTiming = models.TimeField()
    eventCapacity = models.IntegerField()
    eventPriceAdult = models.FloatField()
    eventPriceChild = models.FloatField()
    eventStatus = models.BooleanField()
    eventDisplay = models.BooleanField()

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=250)
    eventTiming = models.TimeField()
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()
    adultsCount = models.IntegerField()
    childrenCount = models.IntegerField()
    paymentID = models.CharField(max_length=250,unique=True)
