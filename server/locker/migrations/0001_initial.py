# Generated by Django 4.1 on 2022-08-19 06:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('start_time', models.SmallIntegerField(default=9, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(12)])),
                ('end_time', models.SmallIntegerField(default=22, validators=[django.core.validators.MinValueValidator(12), django.core.validators.MaxValueValidator(24)])),
                ('small_price', models.SmallIntegerField(default=2000, help_text='무인 사물함의 기본가격을 적어주세요!', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000)])),
                ('mid_price', models.SmallIntegerField(blank=True, null=True)),
                ('big_price', models.SmallIntegerField(blank=True, null=True)),
                ('image', models.ImageField(default='default.png', upload_to='lockers/')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='MeMo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('password', models.CharField(max_length=30)),
                ('usage_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('locker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locker', to='locker.locker')),
            ],
        ),
    ]
