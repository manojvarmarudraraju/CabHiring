from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils import timezone
from datetime import date
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.sessions.backends.db import SessionStore
from selfdrive.models import *
from hiring.models import *
from supervisor.models import *
from users.models import *
from hiring.models import *


def DriverLogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('DriverHome')
        else:
            return redirect('DriverLogin')
    else:
        return render(request,'loginUser.html')
def Driverdetails(request):
    phone = request.user.username
    n = Driverdb.objects.get(mobileno=phone)
    return render(request,'updatedriver.html',{'n':n})
def DriverUpdatedetails(request):
    if request.method=="POST":
        phone = request.user.username
        n = Driverdb.objects.get(mobileno=phone)
        n.firstname = request.POST['firstname']
        n.lastname = request.POST['lastname']
        n.email = request.POST['email']
        n.save()
        return redirect(Driverdetails)
    else:
        return HttpResponse('Hello')


def ViewSalaries(request):
    phone = request.user.username
    n = Driverdb.objects.get(mobileno=phone)
    q=MonthlySalary.objects.filter(Driverid=phone)
    return render(request,'salarydriver.html',{'q':q,'n':n})

def viewslip(request,rownum):
    phone = request.user.username
    n = Driverdb.objects.get(mobileno=phone)
    q = MonthlySalary.objects.get(id=rownum)
    return render(request,'driversal2.html',{'q':q,'n':n})


def DriverHome(request):
    phone = request.user.username
    n = Driverdb.objects.get(mobileno=phone)
    return render(request, 'driverhome.html', {'n': n})


def Driverlogout(request):
    logout(request)
    return redirect('DriverLogin')

def drivermaintanence(request):
    phone = request.user.username
    n = Driverdb.objects.get(mobileno=phone)
    p=drivercar.objects.get(driver_id=phone)
    s=HiringCar.objects.filter(Driverid=p.driver_id)
    return render(request, 'mainatanencecost.html', { 'n': n,'s':s})

def Driverviewbookings(request):
    phone = request.user.username
    n = Driverdb.objects.get(mobileno=phone)
    a=HiringCar.objects.filter(Driverid=phone).filter(status="upcoming")
    b = HiringCar.objects.filter(Driverid=phone).filter(status="completed")
    return render(request,'driverviewbookings.html',{'n':n,'a':a,'b':b})


def startride(request,bookid):
    phone = request.user.username
    n = Driverdb.objects.get(mobileno=phone)
    if HiringCar.objects.filter(Driverid=phone).filter(status="ongoing").exists():
        return redirect('viewongoing')
    else:
        a=HiringCar.objects.get(id=bookid)
        a.status="ongoing"
        a.save()
        return redirect('viewongoing')
def endride(request,bookid):
    if request.method=="POST":
        phone = request.user.username
        a = HiringCar.objects.get(id=bookid)
        price=request.POST['price']
        damage=request.POST['damage']
        damagecost=request.POST['damagecost']
        a.Damage=damage
        a.DamageCost=damagecost
        a.ActualPrice=price
        a.status = "completed"
        a.save()
        return redirect('Driverviewbookings')
    else:
        phone = request.user.username
        n = Driverdb.objects.get(mobileno=phone)
        return render(request,'driverendride.html',{'n':n})


def viewongoing(request):
    phone = request.user.username
    a=HiringCar.objects.filter(Driverid=phone).get(status="ongoing")
    phone = request.user.username
    n = Driverdb.objects.get(mobileno=phone)
    return render(request,'viewongoing.html',{'q':a,'n':n})