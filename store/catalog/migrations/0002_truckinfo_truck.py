# Generated by Django 5.0.1 on 2024-01-09 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TruckInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('mileage', models.IntegerField(blank=True, null=True)),
                ('power', models.IntegerField(blank=True, null=True)),
                ('condition', models.BooleanField(choices=[(0, 'brand new'), (1, 'used')])),
                ('discount', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'TruckInfo',
                'verbose_name_plural': 'TruckInfo',
            },
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('truck_type', models.CharField(blank=True, choices=[('HEAD', 'head'), ('CARGO', 'cargo'), ('DUMP', 'dump')], max_length=10, null=True)),
                ('main_photo', models.ImageField(upload_to='trucks_img/')),
                ('second_photo', models.ImageField(blank=True, null=True, upload_to='trucks_img/')),
                ('third_photo', models.ImageField(blank=True, null=True, upload_to='trucks_img/')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('change_date', models.DateField(auto_now=True)),
                ('sub_catalog', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sub_catalog', to='catalog.subcatalog')),
                ('info', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='truck', to='catalog.truckinfo')),
            ],
            options={
                'verbose_name': 'Truck',
                'verbose_name_plural': 'Trucks',
            },
        ),
    ]