# Generated by Django 2.0.5 on 2019-03-12 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190312_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiringcar',
            name='status',
            field=models.CharField(default='upcoming', max_length=12),
        ),
        migrations.AddField(
            model_name='selfbooking',
            name='status',
            field=models.CharField(default='upcoming', max_length=12),
        ),
    ]
