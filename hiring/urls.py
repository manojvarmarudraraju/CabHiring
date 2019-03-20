from django.urls import path,include
from . import views

urlpatterns=[
path('',views.DriverLogin,name='DriverLogin'),
path('Driverdetails/',views.Driverdetails,name='Driverdetails'),
path('DriverUpdatedetails/',views.DriverUpdatedetails,name='DriverUpdatedetails'),
path('ViewSalaries/',views.ViewSalaries,name='ViewSalaries'),
path('viewslip/<rownum>',views.viewslip,name='viewslip'),
path('DriverHome/',views.DriverHome,name='DriverHome'),
path('Driverlogout/',views.Driverlogout,name='Driverlogout'),
]