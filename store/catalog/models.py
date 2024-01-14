from django.db import models
from django.db.models import SET_NULL, PROTECT

from catalog.constants import HEAD, DUMP, CARGO, LIGHT, BRAKES, ENGINE

NULLABLE = {'null': True, 'blank': True}


class SubCatalog(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    label = models.CharField(max_length=20, verbose_name='Label')
    img = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sub catalog'
        verbose_name_plural = 'Sub catalogs'
        ordering = ('-name',)


class Truck(models.Model):

    TRUCKS_TYPES = [
        (HEAD, 'head'),
        (CARGO, 'cargo'),
        (DUMP, 'dump'),
    ]

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    info = models.OneToOneField('TruckInfo', on_delete=SET_NULL, **NULLABLE, related_name='truck')
    sub_catalog = models.ForeignKey('SubCatalog', on_delete=PROTECT, related_name='truck_sub_catalog')
    type = models.CharField(max_length=10, choices=TRUCKS_TYPES, **NULLABLE)
    main_photo = models.ImageField(upload_to='trucks_img/')
    second_photo = models.ImageField(upload_to='trucks_img/', **NULLABLE)
    third_photo = models.ImageField(upload_to='trucks_img/', **NULLABLE)
    create_date = models.DateField(auto_now_add=True)
    change_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.type}'

    def show_id(self):
        return f'{self.pk:05}'

    class Meta:
        verbose_name = 'Truck'
        verbose_name_plural = 'Trucks'
        ordering = ('pk',)


class TruckInfo(models.Model):

    class Condition(models.IntegerChoices):
        BRAND_NEW = 0, 'brand new'
        USED = 1, 'used'

    year = models.IntegerField(**NULLABLE)
    mileage = models.IntegerField(**NULLABLE)
    power = models.IntegerField(**NULLABLE)
    condition = models.BooleanField(choices=Condition.choices)
    discount = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'TruckInfo'
        verbose_name_plural = 'TruckInfo'


class Part(models.Model):

    PARTS_TYPES = [
        (LIGHT, 'light'),
        (ENGINE, 'engine'),
        (BRAKES, 'brakes'),
    ]

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    info = models.TextField(**NULLABLE)
    sub_catalog = models.ForeignKey('SubCatalog', on_delete=PROTECT, related_name='part_sub_catalog')
    type = models.CharField(max_length=10, choices=PARTS_TYPES, **NULLABLE)
    main_photo = models.ImageField(upload_to='parts_img/')
    create_date = models.DateField(auto_now_add=True)
    change_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Part'
        verbose_name_plural = 'Parts'
        ordering = ('pk',)
