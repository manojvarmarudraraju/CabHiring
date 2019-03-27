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
    return render(request, 'registeradmin.html', {'form': form1})


@login_required
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

@login_required
def AdminHome(request):
    phone = request.user.username
    n = admindb.objects.get(mobileno=phone)
    return render(request, 'adminhome.html', {'n': n})

def AdminLogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            if admindb.objects.filter(mobileno=username).exists():
                login(request, user)
                return redirect('AdminHome')
            elif userdb.objects.filter(mobileno=username).exists():
                return redirect('UserLogin')
            elif Driverdb.objects.filter(mobileno=username).exists():
                return redirect('DriverLogin')
        else:
            return redirect('AdminLogin')
    else:
        return render(request,'Adminlogin.html')


@login_required
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

@login_required
def Adminlogout(request):
    logout(request)
    return redirect('AdminLogin')


@login_required
def admindetails(request):
    phone = request.user.username
    n = admindb.objects.get(mobileno=phone)
    return render(request, 'updateadmin.html', {'n': n})

@login_required
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


@login_required
def setprices(request):
    if request.method=="POST":
        SelfDriveCar.objects.filter(Cartype="sedan").update(ExpectedPrice=request.POST['selfsedanprice'])
        SelfDriveCar.objects.filter(Cartype="micro").update(ExpectedPrice=request.POST['selfmicroprice'])
        SelfDriveCar.objects.filter(Cartype="suv").update(ExpectedPrice=request.POST['selfsuvprice'])
        SelfDriveCar.objects.filter(Cartype="hatchback").update(ExpectedPrice=request.POST['selfhatchbackprice'])
        if HiredCar.objects.filter(Cartype="sedan").exists():
            HiredCar.objects.filter(Cartype="sedan").update(Costperkilometer=request.POST['hiresedanprice'])
        if HiredCar.objects.filter(Cartype="micro").exists():
            HiredCar.objects.filter(Cartype="micro").update(Costperkilometer=request.POST['hiremicroprice'])
        if HiredCar.objects.filter(Cartype="suv").exists():
            HiredCar.objects.filter(Cartype="suv").update(Costperkilometer=request.POST['hiresuvprice'])
        if HiredCar.objects.filter(Cartype="hatchback").exists():
            HiredCar.objects.filter(Cartype="hatchback").update(Costperkilometer=request.POST['hirehatchbackprice'])
        return redirect("AdminHome")
    else:
        phone = request.user.username
        n = admindb.objects.get(mobileno=phone)
        return render(request, 'setprices.html', {'n': n})


@login_required
def selfbookings(request):
    phone = request.user.username
    n = admindb.objects.get(mobileno=phone)
    sb=SelfBooking.objects.filter(status="upcoming").order_by('Userid')
    sh = SelfBooking.objects.filter(status="completed").order_by('Userid')
    return render(request,'viewselfbookadmin.html',{'n':n,'sb':sb,'sb2':sh})

@login_required
def hirebookings(request):
    phone = request.user.username
    n = admindb.objects.get(mobileno=phone)
    hb=HiringCar.objects.filter(status="upcoming").order_by('Userid')
    return render(request,'viewhirebookadmin.html',{'n':n,'hb':hb})

@login_required
def cancelself(request,bookid):
    sc=SelfBooking.objects.filter(id=bookid)
    sc.delete()
    return redirect('selfbookings')

@login_required
def cancelhire(request,bookid):
    sc=HiringCar.objects.filter(id=bookid)
    sc.delete()
    return redirect('hirebookings')

@login_required
def maintanenceself(request):
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
    return render(request,'maintanenceself.html',{'y':y,'n':n})


@login_required
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
    return render(request, 'maintanencehire.html',{'y':y,'n':n})

@login_required
def deleteselfcar(request,carid):
    SelfBooking.objects.filter(Carid=carid).delete()
    SelfCancelrepo.objects.filter(Carid=carid).delete()
    SelfDriveCar.objects.filter(CarRegistration=carid).delete()
    SelfDriveMaintanence.objects.filter(CarReg=carid)
    Maintanencecost.objects.get(carid=carid).delete()
    return redirect('maintanenceself')

@login_required
def driverratings(request):
    phone = request.user.username
    n = admindb.objects.get(mobileno=phone)
    r = Maintanencecost.objects.filter(type="hire")
    for i in r:
        carid = i.carid
        p=drivercar.objects.get(car_id=carid)
        driver=p.driver_id
        q = HiringCar.objects.filter(Driverid=driver)
        total = 0
        i=0
        for p in q:
            total = total + p.DriverRating
            i+=1
        a = Maintanencecost.objects.get(carid=carid)
        b=Driverdb.objects.get(mobileno=driver)
        if i!=0:
            b.rating=int(total/i)
            b.save()
        else:
            b.rating=0
            b.save()
        a.rating = total
        a.save()

    y=Driverdb.objects.all().order_by('rating')
    return render(request, 'driverrating.html', {'y': y,'n':n})


@login_required
def removedriver(request,driverid):
    HiringCar.objects.filter(Driverid=driverid).delete()
    HireCancelrepo.objects.filter(Driverid=driverid).delete()
    d=drivercar.objects.get(driver_id=driverid)
    cid=d.car_id
    drivercar.objects.filter(driver_id=driverid).delete()
    HiredCar.objects.filter(HcarRegistration=cid).delete()
    Driverdb.objects.filter(mobileno=driverid).delete()
    Maintanencecost.objects.filter(carid=cid).delete()
    return redirect('AdminHome')


@login_required
def selfviewbooking(request,bookid):
    sc = SelfBooking.objects.get(id=bookid)
    return render(request,'test.html',{'sc':sc})

@login_required
def hireviewbooking(request,bookid):
    sc = HiringCar.objects.get(id=bookid)
    return render(request,'test.html',{'sc':sc})

@login_required
def checkavailability(request):
    a=HiredCar.objects.filter(availability="yes")
    b=HiredCar.objects.filter(availability="no")
    return render(request,'checkavailability.html',{'a':a,'b':b})

@login_required
def setavailability(request,carid):
    a = HiredCar.objects.get(HcarRegistration=carid)
    avai=a.availability
    if avai=="yes":
        HiredCar.objects.filter(HcarRegistration=carid).update(availability="no")
    else:
        HiredCar.objects.filter(HcarRegistration=carid).update(availability="yes")
    return redirect('checkavailability')