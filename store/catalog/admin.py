from django.contrib import admin

from catalog.models import SubCatalog, Truck, Part, TruckInfo


@admin.register(SubCatalog)
class SubCatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'label', 'img')


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'truck_type', 'main_photo')


@admin.register(TruckInfo)
class TruckInfoAdmin(admin.ModelAdmin):
    list_display = ('year', 'mileage', 'power', 'condition', 'discount')


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'part_type', 'main_photo')
