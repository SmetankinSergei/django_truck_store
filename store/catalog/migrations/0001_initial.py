# Generated by Django 5.0.1 on 2024-01-09 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('label', models.CharField(max_length=20, verbose_name='Label')),
                ('img', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Sub catalog',
                'verbose_name_plural': 'Sub catalogs',
                'ordering': ('-name',),
            },
        ),
    ]