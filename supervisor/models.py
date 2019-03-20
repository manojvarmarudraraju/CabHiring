from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class admindb(models.Model):
    admin=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=12)
    email=models.EmailField()

class Maintanencecost(models.Model):
    carid=models.CharField(max_length=15,default="")
    cost=models.IntegerField(default=0)
    type=models.CharField(default="self",max_length=5)
    rating=models.IntegerField(default=0)
