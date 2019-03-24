from django.test import TestCase
from django.urls import resolve
from .views import *
from .models import *
from django.test import SimpleTestCase,TestCase
from django.urls import reverse,resolve
from .views import *
from .models import *
from django.test.client import RequestFactory
from selfdrive.models import *
from django.utils import timezone
import base64
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_UserLogin_url_is_resolved(self):
        url=reverse('UserLogin')
        print(resolve(url))
        self.assertEquals(resolve(url).func,UserLogin)
    def test__UserRegister_url_is_resolved(self):
        url=reverse('UserRegister')
        print(resolve(url))
        self.assertEquals(resolve(url).func, UserRegister)
    def test__UserLOgout_url_is_resolved(self):
        url=reverse('Userlogout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, Userlogout)
    def test__UserDetailsView_url_is_resolved(self):
        url=reverse('UserDetailsView')
        print(resolve(url))
        self.assertEquals(resolve(url).func, UserDetailsView)
    def test__UpdateDetails_url_is_resolved(self):
        url=reverse('UpdateDetails')
        print(resolve(url))
        self.assertEquals(resolve(url).func, UpdateDetails)
    def test__sbookcar_url_is_resolved(self):
        carid="ap37cn0910"
        url=reverse('sbookcar',args=(carid,))
        print(resolve(url))


class Model_testing(TestCase):
    def create_user(self,user_id="9440711733",firstname="Manoj",lastname="Varma",mobileno="9440711733",birthdate="2019-02-06",email="manojrudraraju007@gmail.com",pincode="534202",gender=0):
        return userdb.objects.create(firstname=firstname,lastname=lastname,mobileno=mobileno,birthdate=birthdate,email=email,pincode=pincode,gender=gender,user_id=user_id)
    def create_username(self,mobileno="9440711733",password="my_secret"):
        self.request_factory = RequestFactory()
        return User.objects.create_user(username=mobileno, email='javed@javed.com', password=password)
    def test_userdb_creation(self):
        a=self.create_user()
        self.assertTrue(isinstance(a,userdb))
        self.assertEquals(a.__str__(),a.mobileno)
    def create_selfdrive(self):
        SelfDriveCar.objects.create(CarRegistration="AP37CN0000",CarCompany="Toyota",CarName="Etios",CarCapacity=5,Cartype="sedan",
                                    carpreowned=base64.encodebytes('foo'.encode()),CarBoughtDate=timezone.now(),CarDescription="")
        SelfDriveCar.objects.create(CarRegistration="AP37CN0001", CarCompany="Toyota", CarName="Etios", CarCapacity=5,
                                    Cartype="micro",
                                    carpreowned=base64.encodebytes('foo'.encode()), CarBoughtDate=timezone.now(), CarDescription="")
        SelfDriveCar.objects.create(CarRegistration="AP37CN0002", CarCompany="Toyota", CarName="Etios", CarCapacity=5,
                                    Cartype="hatchback",
                                    carpreowned=base64.encodebytes('foo'.encode()), CarBoughtDate=timezone.now(), CarDescription="")
        SelfDriveCar.objects.create(CarRegistration="AP37CN0003", CarCompany="Toyota", CarName="Etios", CarCapacity=5,
                                    Cartype="suv",
                                    carpreowned=base64.encodebytes('foo'.encode()), CarBoughtDate=timezone.now(), CarDescription="")
    def create_hiredrive(self):
        HiredCar.objects.create(HcarRegistration="AP37CN0004",  CarName="Etios", Cartype="sedan",
                         CarCapacity=5,CarCompany="Toyota")
        HiredCar.objects.create(HcarRegistration="AP37CN0005", CarName="Etios", Cartype="micro",
                                CarCapacity=5, CarCompany="Toyota")
        HiredCar.objects.create(HcarRegistration="AP37CN0006", CarName="Etios", Cartype="hatchback",
                                CarCapacity=5, CarCompany="Toyota")
        HiredCar.objects.create(HcarRegistration="AP37CN0007", CarName="Etios", Cartype="suv",
                                CarCapacity=5, CarCompany="Toyota")
    def test_UserRegister_view(self):
        a=self.create_user()
        url=reverse('UserRegister')
        res=self.client.get(url)
        self.assertEquals(res.status_code,200)
        self.assertTemplateUsed(res,'registerUser1.html')
        form_data = {'username': "9440711733", 'password1': "iamthegreat02", 'password2': "iamthegreat02"}
        form = UserForm(data=form_data)
        p = self.client.post(url, data={'firstname': "Manoj", 'lastname': "varma", 'mobileno': "9440711733",
                                        'dob': "2019-02-06", 'email': "manojrudraraju007@gmail.com", 'pin': "534202",
                                        'optradio': 0,'username': "9440711733", 'password1': "iamthegreat02", 'password2': "iamthegreat02"}, follow=True)
        self.assertRedirects(p,'/user/Userhome/')

    def test_UserLogin_view(self):
        a = self.create_user()
        url = reverse('UserLogin')
        r=self.client.get(url)
        self.assertTemplateUsed(r,'loginUser.html')

    def test_UserLogout_view(self):
        url = reverse('Userlogout')
        r = self.client.get(url)
        self.assertRedirects(r,'/user/')

    def test_UserDetailsView(self):
        count = User.objects.count()
        b=self.create_username()
        a = self.create_user()
        self.client.login(username="9440711733", password="my_secret")
        self.assertTrue(a)
        self.assertEqual(User.objects.count(),count+1)
        url=reverse('UserDetailsView')
        r=self.client.get(url)
        self.assertTemplateUsed(r,'UserDetailsUpdation.html')

    def test_Userhome(self):
        b = self.create_username()
        a = self.create_user()
        self.client.login(username="9440711733", password="my_secret")
        url = reverse('Userhome')
        r = self.client.get(url)
        self.assertTemplateUsed(r, 'userhome.html')
    def test_updatedetails(self):
        b = self.create_username()
        a = self.create_user()
        self.client.login(username="9440711733", password="my_secret")
        url=reverse('UpdateDetails')
        r=self.client.post(url,{'firstname':"ManojVarma",'lastname':"Rudraraju",'pin':"544444",'email':"manoj@gmail.com"})
        self.assertTrue(r)
    def test_cartype(self):
        b = self.create_username()
        a = self.create_user()
        self.client.login(username="9440711733", password="my_secret")
        url = reverse('Cartype')
        r=self.client.get(url)
        self.assertTemplateUsed(r,'test.html')
        w=self.client.post(url,{'type':"selfdrive"})
        self.assertRedirects(w,'/user/sviewcars')
    def test_sviewcars(self):
        b = self.create_username()
        a = self.create_user()
        self.client.login(username="9440711733", password="my_secret")
        url=reverse('sviewcars')
        self.create_selfdrive()
        r=self.client.get(url)
        self.assertTemplateUsed(r,'selfdrives.html')
    def test_hviewcars(self):
        b = self.create_username()
        a = self.create_user()
        self.client.login(username="9440711733", password="my_secret")
        url=reverse('hviewcars')
        self.create_hiredrive()
        r=self.client.get(url)
        self.assertTemplateUsed(r,'hiredrives.html')
    def test_sbookcar(self):
        carid = "AP37CN0001"
        b = self.create_username()
        a = self.create_user()
        self.create_selfdrive()
        self.client.login(username="9440711733", password="my_secret")
        url = reverse('sbookcar', args=(carid,))
        q=self.client.get(url)
        self.assertTemplateUsed(q,'selfbook.html')
        w=self.client.post(url,{'address':"  ",'days':2,'time':13,'date':timezone.now()})
        self.assertRedirects(w,'/user/Userhome/')
    