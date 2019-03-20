from django.db import models
from django.contrib.auth.models import User

class Driverdb(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE);
    firstname = models.CharField(max_length=30);
    lastname = models.CharField(max_length=30);
    mobileno = models.IntegerField(primary_key=True);
    gender = models.IntegerField();
    bloodgroup = models.CharField(max_length=5);
    birthdate = models.DateField();
    address = models.CharField(max_length=2000);
    city = models.CharField(max_length=30);
    state = models.CharField(max_length=30);
    pincode = models.IntegerField();
    email = models.EmailField();
    BaseSalary=models.IntegerField(default=0)
    AccountNo=models.CharField(default='',max_length=10)
    IfscCode=models.CharField(default='',max_length=12)



class HiredCar(models.Model):

    HcarRegistration=models.CharField(max_length=10,primary_key=True,default='AP37CJ2900')
    CarCompany=models.CharField(max_length=30,default="maruti")
    CarName=models.CharField(max_length=30)
    CarCapacity=models.IntegerField();
    Cartype=models.CharField(max_length=10)
    CarDescription=models.CharField(max_length=300,default='')
    image=models.URLField(max_length=500, blank=True, default='')
    status=models.IntegerField(default=0)
    Costperkilometer=models.IntegerField(default=0)



class MonthlySalary(models.Model):
    Driverid=models.IntegerField()
    Date=models.DateTimeField()
    Salary=models.IntegerField()
    year=models.IntegerField(default=2019)
    month=models.CharField(max_length=15,default='january')




class drivercar(models.Model):
    driver=models.ForeignKey(Driverdb,on_delete=models.CASCADE)
    car=models.ForeignKey(HiredCar,on_delete=models.CASCADE)
    class Meta:
        unique_together = (('driver', 'car'),)

