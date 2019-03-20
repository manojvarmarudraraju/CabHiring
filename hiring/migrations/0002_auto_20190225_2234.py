# Generated by Django 2.0.5 on 2019-02-25 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hiring', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driverdb',
            fields=[
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('mobileno', models.IntegerField(primary_key=True, serialize=False)),
                ('gender', models.IntegerField()),
                ('bloodgroup', models.CharField(max_length=5)),
                ('birthdate', models.DateField()),
                ('address', models.CharField(max_length=2000)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('BaseSalary', models.IntegerField(default=0)),
                ('AccountNo', models.CharField(default='', max_length=10)),
                ('IfscCode', models.CharField(default='', max_length=12)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HiredCar',
            fields=[
                ('HcarRegistration', models.CharField(default='AP37CJ2900', max_length=10, primary_key=True, serialize=False)),
                ('CarCompany', models.CharField(max_length=30)),
                ('CarName', models.CharField(max_length=30)),
                ('CarCapacity', models.IntegerField()),
                ('Cartype', models.CharField(max_length=10)),
                ('carpreowned', models.BinaryField()),
                ('CarBoughtDate', models.DateTimeField()),
                ('CarDescription', models.CharField(max_length=300)),
                ('image', models.URLField(blank=True, default='', max_length=500)),
                ('status', models.IntegerField(default=0)),
                ('Costperkilometer', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MonthlySalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Driverid', models.IntegerField()),
                ('Date', models.DateTimeField()),
                ('Salary', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='HiringCar',
        ),
        migrations.DeleteModel(
            name='SelfBooking',
        ),
        migrations.RemoveField(
            model_name='userdb',
            name='user',
        ),
        migrations.DeleteModel(
            name='userdb',
        ),
        migrations.AlterUniqueTogether(
            name='monthlysalary',
            unique_together={('Driverid', 'Date')},
        ),
    ]