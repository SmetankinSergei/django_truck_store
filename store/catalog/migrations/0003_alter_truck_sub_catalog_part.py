# Generated by Django 5.0.1 on 2024-01-09 19:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_truckinfo_truck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='sub_catalog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='truck_sub_catalog', to='catalog.subcatalog'),
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('info', models.TextField(blank=True, null=True)),
                ('part_type', models.CharField(blank=True, choices=[('LIGHT', 'light'), ('ENGINE', 'engine'), ('BRAKES', 'brakes')], max_length=10, null=True)),
                ('main_photo', models.ImageField(upload_to='parts_img/')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('change_date', models.DateField(auto_now=True)),
                ('sub_catalog', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='part_sub_catalog', to='catalog.subcatalog')),
            ],
            options={
                'verbose_name': 'Part',
                'verbose_name_plural': 'Parts',
            },
        ),
    ]
