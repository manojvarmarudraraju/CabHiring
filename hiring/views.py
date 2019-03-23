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


def DriverLogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect('DriverHome')
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

def maintanence(request):
    phone = request.user.username
    n = Driverdb.objects.get(mobileno=phone)
    p=drivercar.objects.get(driver_id=phone)
    r = Maintanencecost.objects.filter(type="hire")

    return render(request, 'test.html', { 'n': n})
