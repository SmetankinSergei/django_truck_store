from django import template

from catalog.models import SubCatalog, Truck, Part

register = template.Library()


CATALOG_ITEMS = {'trucks': Truck, 'parts': Part}


@register.simple_tag()
def get_sub_catalogs():
    return SubCatalog.objects.all()


@register.simple_tag()
def get_catalog_items(sub_catalog_name, item_type):
    if item_type == 'all types':
        return CATALOG_ITEMS[sub_catalog_name].objects.all()
    else:
        return CATALOG_ITEMS[sub_catalog_name].objects.filter(type=item_type.upper())


@register.simple_tag()
def main_photo_path_tag(item):
    return item.main_photo.url


@register.filter()
def main_photo_path(item_photo_path):
    return item_photo_path.url
