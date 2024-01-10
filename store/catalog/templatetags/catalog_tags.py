from django import template

from catalog.models import SubCatalog, Truck, Part

register = template.Library()


CATALOG_ITEMS = {'trucks': Truck, 'parts': Part}


@register.simple_tag()
def get_sub_catalogs():
    return SubCatalog.objects.all()


@register.simple_tag()
def get_trucks():
    return Truck.objects.all()


@register.simple_tag()
def get_parts():
    return Part.objects.all()


@register.simple_tag()
def get_catalog_items(sub_catalog_name):
    return CATALOG_ITEMS[sub_catalog_name].objects.all()
