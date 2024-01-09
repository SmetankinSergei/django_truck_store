from django.contrib import admin

from catalog.models import SubCatalog


@admin.register(SubCatalog)
class SubCatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'label', 'img')
