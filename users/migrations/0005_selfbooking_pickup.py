# Generated by Django 2.0.5 on 2019-02-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_selfbooking_ti'),
    ]

    operations = [
        migrations.AddField(
            model_name='selfbooking',
            name='pickup',
            field=models.CharField(default='', max_length=300),
        ),
    ]