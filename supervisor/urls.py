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
path('maintanenceself/',views.maintanenceself,name='maintanenceself'),
path('maintanencehire/',views.maintanencehire,name='maintanencehire'),
path('setprices/',views.setprices,name='setprices'),
path('selfbookings/',views.selfbookings,name='selfbookings'),
path('hirebookings/',views.hirebookings,name='hirebookings'),
path('cancelself/<bookid>',views.cancelself,name='cancelself'),
path('cancelhire/<bookid>',views.cancelhire,name='cancelhire'),
path('deleteselfcar/<carid>',views.deleteselfcar,name='deleteselfcar'),
path('driverratings/',views.driverratings,name='driverratings'),
path('removedriver/<driverid>',views.removedriver,name='removedriver'),
path('selfviewbooking/<bookid>',views.selfviewbooking,name='selfviewbooking'),
path('hireviewbooking/<bookid>',views.hireviewbooking,name='hireviewbooking'),
path('checkavailability/',views.checkavailability,name='checkavailability'),
path('setavailability/<carid>',views.setavailability,name='setavailability')
        ]