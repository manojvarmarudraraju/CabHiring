from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils import timezone
from datetime import date
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from supervisor.models import *
from django.contrib.sessions.backends.db import SessionStore
from selfdrive.models import *
from hiring.models import *
from .forms import *
import datetime
from users.models import *
def adminregister(request):
    if request.method=="POST":
        form1=AdminForm(request.POST)
        if form1.is_valid():
            form1.save()
            phone = form1.cleaned_data['username']
            password = form1.cleaned_data['password1']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            mobileno=phone
            email=request.POST['email']
            user=authenticate(username=phone,password=password)
            login(request,user)
            t=admindb(admin_id=user.id,firstname=firstname,lastname=lastname,mobileno=mobileno,email=email)
            t.save()
            return redirect(AdminHome)
    else:
        form1 = AdminForm()
    return render(request, 'registerUser1.html', {'form': form1})

def adddriver(request):
    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            phone = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            dob = request.POST['dob']
            gender = request.POST['gender']
            pincode = request.POST['pin']
            mobile = request.POST['mobile']
            city = request.POST['city']
            state = request.POST['state']
            accnum = request.POST['accnum']
            ifsc = request.POST['ifsc']
            email = request.POST['email']
            basesalary = request.POST['base']
            bloodgroup = request.POST['blood']
            address = request.POST['address']
            driver = authenticate(username=phone, password=password)
            w = Driverdb(driver_id=driver.id, firstname=firstname, lastname=lastname, gender=gender, mobileno=mobile,
                         bloodgroup=bloodgroup, birthdate=dob,
                         address=address, city=city, state=state, pincode=pincode, email=email, BaseSalary=basesalary,
                         AccountNo=accnum, IfscCode=ifsc)
            w.save()
            registration = request.POST['registration']
            #company = request.POST['company']
            carmodel = request.POST['carmodel']
            cartype = request.POST['cartype']
            capacity = request.POST['capacity']
            e = HiredCar(HcarRegistration=registration,  CarName=carmodel, Cartype=cartype,
                         CarCapacity=capacity)
            e.save()
            driver_id = mobile
            car_id = registration
            r = drivercar(driver_id=driver_id, car_id=car_id)
            r.save()
            p=Maintanencecost(carid=registration,cost=0,type="hire")
            p.save()
            return redirect(AdminHome)
        else:
            return render(request,'test2.html')

    else:
        form = DriverForm()
    return render(request, 'RegisterADriver.html', {'form': form})


def AdminHome(request):
    phone = request.user.username
    n = admindb.objects.get(mobileno=phone)
    return render(request, 'adminhome.html', {'n': n})

def AdminLogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)

        login(request, user)
        return redirect(AdminHome)
    else:
        return render(request,'Adminlogin.html')



def IssueSalary(request):
    if request.method=="POST":
        a=Driverdb.objects.all()
        month=request.POST['month']
        year=request.POST['year']
        for i in a:
            #today = datetime.date.today()
            #b=HiringCar.objects.get(Driverid=i.mobileno)
            #total=0
            #for j in b:
                #total=total+j.ActualPrice
            total=i.BaseSalary#+total
            t=MonthlySalary(Driverid=i.mobileno,Date=timezone.now(),month=month,year=year,Salary=total)
            t.save()
        return redirect(AdminHome)
    else:
        phone = request.user.username
        n = admindb.objects.get(mobileno=phone)
        return render(request,'salaryadmin.html',{'n':n})


def Adminlogout(request):
    logout(request)
    return redirect('AdminLogin')

def admindetails(request):
    phone = request.user.username
    n = admindb.objects.get(mobileno=phone)
    return render(request, 'updateadmin.html', {'n': n})

def adminupdatedetails(request):
    if request.method=="POST":
        phone = request.user.username
        n = admindb.objects.get(mobileno=phone)
        n.firstname = request.POST['firstname']
        n.lastname = request.POST['lastname']
        n.email = request.POST['email']
        n.save()
        return redirect(admindetails)
    else:
        return HttpResponse('Hello')

def setprices(request):
    if request.method=="POST":
        w=SelfDriveCar.objects.all()
        for i in w:
            if i.Cartype=="sedan":
                i.ExpectedPrice=request.POST['selfsedanprice']
            elif i.Cartype=="micro":
                i.ExpectedPrice = request.POST['selfmicroprice']
            elif i.Cartype=="hatchback":
                i.ExpectedPrice = request.POST['selfhatchbackprice']
            elif i.Cartype=="suv":
                i.ExpectedPrice = request.POST['selfsuvprice']
            i.save()
        e=HiredCar.objects.all()
        for i in e:
            if i.Cartype=="sedan":
                i.Costperkilometer=request.POST['hiresedanprice']
            elif i.Cartype=="micro":
                i.Costperkilometer = request.POST['hiremicroprice']
            elif i.Cartype=="hatchback":
                i.Costperkilometer = request.POST['hirehatchbackprice']
            elif i.Cartype=="suv":
                i.Costperkilometer = request.POST['hiresuvprice']
            i.save()
        return redirect("AdminHome")
    else:
        phone = request.user.username
        n = admindb.objects.get(mobileno=phone)
        return render(request, 'setprices.html', {'n': n})



def selfbookings(request):
    phone = request.user.username
    n = admindb.objects.get(mobileno=phone)
    sb=SelfBooking.objects.filter(status="upcoming")
    return render(request,'viewselfbookadmin.html',{'n':n,'sb':sb})
def selfbookings(request):
    phone = request.user.username
    n = admindb.objects.get(mobileno=phone)
    sb=HiringCar.objects.filter(status="upcoming")
    return render(request,'viewselfbookadmin.html',{'n':n,'sb':sb})
def cancelself(request,bookid):
    sc=SelfBooking.objects.filter(id=bookid)
    sc.delete()
    return redirect('selfbookings')
def cancelhire(request,bookid):
    sc=HiringCar.objects.filter(id=bookid)
    sc.delete()
    return redirect('selfbookings')
def maintainenceself(request):
    phone = request.user.username
    n = admindb.objects.get(mobileno=phone)
    r=Maintanencecost.objects.filter(type="self")
    for i in r:
        carid=i.carid
        q=SelfBooking.objects.filter(Carid=carid)
        total=0
        for p in q:
            total=total+p.DamageCost
        a = Maintanencecost.objects.get(carid=carid)
        a.cost=total
        a.save()
    y = Maintanencecost.objects.filter(type="self").order_by('cost')
    return render(request,'maintainenceself.html',{'y':y,'n':n})

def maintanencehire(request):
    phone = request.user.username
    n = admindb.objects.get(mobileno=phone)
    r = Maintanencecost.objects.filter(type="hire")
    for i in r:
        carid = i.carid
        w=drivercar.objects.get(car_id=carid)
        q = HiringCar.objects.filter(Driverid=w.driver_id)
        total = 0
        for p in q:
            total = total + p.DamageCost
        a = Maintanencecost.objects.get(carid=carid)
        a.cost = total
        a.save()
    y = Maintanencecost.objects.filter(type="hire").order_by('cost')
    return render(request, 'test.html',{'y':y,'n':n})

def deleteselfcar(request,carid):
    SelfBooking.objects.filter(Carid=carid).delete()
    SelfCancelrepo.objects.filter(Carid=carid).delete()
    SelfDriveCar.objects.filter(CarRegistration=carid).delete()
    SelfDriveMaintanence.objects.filter(CarReg=carid)
    return redirect('AdminHome')

def driverratings(request):
    phone = request.user.username
    n = admindb.objects.get(mobileno=phone)
    r = Maintanencecost.objects.filter(type="hire")
    for i in r:
        carid = i.carid
        q = HiringCar.objects.filter(Carid=carid)
        total = 0
        for p in q:
            total = total + p.DriverRating
        a = Maintanencecost.objects.get(carid=carid)
        a.rating = total
        a.save()
    y = Maintanencecost.objects.filter(type="self").order_by('rating')
    return render(request, 'driverrating.html', {'y': y,'n':n})

def removedriver(request,carid):
    HiringCar.objects.filter(Carid=carid).delete()
    HireCancelrepo.objects.filter(Carid=carid).delete()
    d=drivercar.objects.get(CarReg=carid)
    did=d.driver_id
    drivercar.objects.filter(CarReg=carid).delete()
    HiredCar.objects.filter(HcarRegistration=carid)
    Driverdb.objects.filter(mobileno=did).delete()
    return redirect('AdminHome')
