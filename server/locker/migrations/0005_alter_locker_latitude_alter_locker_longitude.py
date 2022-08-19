# Generated by Django 4.1 on 2022-08-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0004_locker_latitude_locker_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locker',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=8),
        ),
        migrations.AlterField(
            model_name='locker',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
    ]