from django.urls import path,include
from . import views

urlpatterns=[
path('UserRegister/',views.UserRegister,name='UserRegister'),
path('',views.UserLogin,name='UserLogin'),
path('UserDetailsView/',views.UserDetailsView,name='UserDetailsView'),
path('Userhome/',views.UserHome,name='Userhome'),
path('UpdateDetails',views.UpdateDetails,name='UpdateDetails'),
path('Cartype',views.Cartype,name='Cartype'),
path('sviewcars',views.sviewcars,name='sviewcars'),
path('hviewcars',views.hviewcars,name='hviewcars'),
path('sbookcar/<carid>',views.sbookcar,name='sbookcar'),
path('hbookcar/<registration>',views.hbookcar,name='hbookcar'),
path('Userlogout/',views.Userlogout,name='Userlogout'),
path('Selfviewbookings/',views.Selfviewbookings,name='Selfviewbookings'),
path('Hireviewbookings/',views.Hireviewbookings,name='Hireviewbookings'),
path('selfcancelbooking/<bookid>',views.selfcancelbooking,name='selfcancelbooking'),
path('editselfbooking/<bookid>',views.editselfbooking,name='editselfbooking'),
path('edithirebooking/<bookid>',views.edithirebooking,name='edithirebooking'),
path('hirecancelbooking/<bookid>',views.hirecancelbooking,name='hirecancelbooking'),
path('selfcarrating/<bookid>',views.selfcarrating,'selfcarrating'),
path('hirecarrating/<bookid>',views.hirecarrating,'hirecarrating')
        ]