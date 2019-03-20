from django.db import models

# Create your models here.
class SelfDriveCar(models.Model):

    CarRegistration=models.CharField(max_length=10,primary_key=True)
    CarCompany=models.CharField(max_length=30)
    CarName=models.CharField(max_length=30)
    CarCapacity=models.IntegerField()
    Cartype=models.CharField(max_length=10)
    carpreowned=models.BinaryField()
    CarBoughtDate=models.DateTimeField()
    CarDescription=models.CharField(max_length=300)
    image=models.URLField(max_length=500, blank=True, default='')
    CarCost=models.IntegerField(default=0)
    Status=models.IntegerField(default=0)
    ExpectedPrice = models.IntegerField(default=0)


class SelfDriveMaintanence(models.Model):
    CarReg = models.CharField(max_length=10)
    Date=models.DateTimeField()
    Cost=models.IntegerField()

    class Meta:
        unique_together = (('CarReg', 'Date'),)
