from django.shortcuts import render

from catalog.constants import ITEMS_TYPES_DATA
from catalog.models import Truck, Part


def catalog(request):
    return render(request, 'catalog/catalog.html')


def sub_catalog(request, section_name, previous_section, sub_catalog_name, prev_item_type):
    page_data = {
        'title': 'MAN - Catalog',
        'section_name': section_name,
        'previous_section': 'catalog',
        'sub_catalog_name': sub_catalog_name,
        'is_sub_section': True,
        'types_data': ITEMS_TYPES_DATA[sub_catalog_name],
        'prev_item_type': prev_item_type,
    }
    return render(request, 'catalog/sub_catalog.html', page_data)


def show_sub_catalog_by_type(request, sub_catalog_name, item_type, prev_item_type):
    page_data = {
        'title': 'MAN - Catalog',
        'section_name': 'catalog',
        'previous_section': 'catalog',
        'sub_catalog_name': sub_catalog_name,
        'is_sub_section': True,
        'types_data': ITEMS_TYPES_DATA[sub_catalog_name],
        'item_type': item_type,
        'prev_item_type': prev_item_type,
    }
    return render(request, 'catalog/show_sub_catalog_by_type.html', page_data)


def item(request, item_id, current_catalog):
    CATALOG_TABLES = {'trucks': Truck, 'parts': Part}
    catalog_item = CATALOG_TABLES[current_catalog].objects.get(pk=item_id)
    page_data = {
        'title': 'MAN - Catalog item',
        'section_name': 'catalog',
        'previous_section': 'catalog',
        'current_catalog': current_catalog,
        'is_sub_section': True,
        'item': catalog_item,
    }
    return render(request, 'catalog/item.html', page_data)
