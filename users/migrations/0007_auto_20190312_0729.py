# Generated by Django 2.0.5 on 2019-03-12 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190303_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiringcar',
            name='rated',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='selfbooking',
            name='rated',
            field=models.IntegerField(default=0),
        ),
    ]
