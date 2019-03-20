from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import time
# Create your models here.
class userdb(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    mobileno=models.CharField(max_length=10,primary_key=True)
    birthdate=models.DateField()
    email=models.EmailField()
    pincode=models.CharField(max_length=7,default="")
    gender=models.IntegerField(default=0)
    def __str__(self):
        return self.mobileno

class SelfBooking(models.Model):
    Carid=models.CharField(max_length=10)
    Userid=models.CharField(max_length=10)
    bookingdate=models.DateTimeField()
    pickup=models.CharField(max_length=300,default="")
    time= models.DateTimeField()
    ti=models.IntegerField(default=0)
    Days=models.IntegerField(default=0)
    ActualPrice=models.IntegerField(default=0)
    ServiceRating=models.IntegerField(default=10)
    ServiceDesc = models.CharField(max_length=50, default='')
    CarRating=models.IntegerField(default=10)
    CarDesc=models.CharField(max_length=50,default='')
    Damage = models.CharField(max_length=50, default='')
    DamageCost = models.IntegerField(default=0)
    rated=models.IntegerField(default=0)
    status = models.CharField(default="upcoming",max_length=12)



class HiringCar(models.Model):
    Driverid=models.CharField(max_length=12)
    Userid=models.CharField(max_length=12)
    Pickup=models.CharField(max_length=300)
    Time=models.IntegerField(default=0)
    Date=models.DateTimeField()
    ExpectedPrice=models.IntegerField(default=0)
    ActualPrice=models.IntegerField(default=0)
    DriverRating=models.IntegerField(default=10)
    DriverDesc=models.CharField(max_length=50,default='')
    ServiceRating=models.IntegerField(default=10)
    ServiceDesc=models.CharField(max_length=50,default='')
    Damage=models.CharField(max_length=50,default='')
    DamageCost=models.IntegerField(default=0)
    rated=models.IntegerField(default=0)
    status=models.CharField(default="upcoming",max_length=12)
    class Meta:
        unique_together = (('Driverid', 'Userid','Date'),)


class SelfCancelrepo(models.Model):
    bookid=models.IntegerField(default=0)
    reason=models.CharField(default="",max_length=100)
    Carid = models.CharField(max_length=12,default="")
    Userid = models.CharField(max_length=12,default="")
    bookingdate = models.DateTimeField()



class HireCancelrepo(models.Model):
    bookid = models.IntegerField(default=0)
    reason = models.CharField(default="", max_length=100)
    Driverid = models.CharField(max_length=12, default="")
    Userid = models.CharField(max_length=12, default="")
