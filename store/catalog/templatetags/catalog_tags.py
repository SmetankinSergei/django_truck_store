from django import template

from catalog.models import SubCatalog, Truck, Part

register = template.Library()


@register.simple_tag()
def get_sub_catalogs():
    return SubCatalog.objects.all()


@register.simple_tag()
def get_trucks():
    return Truck.objects.all()


@register.simple_tag()
def get_parts():
    return Part.objects.all()
