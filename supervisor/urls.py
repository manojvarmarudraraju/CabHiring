from . import views
from django.urls import path,include
urlpatterns=[
path('AdminHome/',views.AdminHome,name='AdminHome'),
path('adddriver/',views.adddriver,name='adddriver'),
path('adminregister/',views.adminregister,name='adminregister'),
path('',views.AdminLogin,name='AdminLogin'),
path('IssueSalary/',views.IssueSalary,name='IssueSalary'),
path('Adminlogout/',views.Adminlogout,name='Adminlogout'),
path('admindetails/',views.admindetails,name='admindetails'),
path('adminupdatedetails/',views.adminupdatedetails,name='adminupdatedetails'),
path('maintainenceself/',views.maintainenceself,name='maintainenceself'),
path('maintanencehire/',views.maintanencehire,name='maintanencehire'),
path('setprices/',views.setprices,name='setprices')
        ]