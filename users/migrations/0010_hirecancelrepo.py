# Generated by Django 2.0.5 on 2019-03-12 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_selfcancelrepo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HireCancelrepo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookid', models.IntegerField(default=0)),
                ('reason', models.CharField(default='', max_length=100)),
                ('Driverid', models.CharField(default='', max_length=12)),
                ('Userid', models.CharField(default='', max_length=12)),
            ],
        ),
    ]