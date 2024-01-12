from django.shortcuts import render

from catalog.constants import ITEMS_TYPES_DATA, SUB_CATALOG_CONTEXT
from catalog.models import Truck, Part
from catalog.templatetags.catalog_tags import get_catalog_items


def catalog(request):
    return render(request, 'catalog/catalog.html')


def sub_catalog(request, sub_catalog_name, current_item_type, prev_item_type):
    context = {
        'sub_catalog_name': sub_catalog_name,
        'types_data': ITEMS_TYPES_DATA[sub_catalog_name],
        'current_item_type': current_item_type,
        'prev_item_type': prev_item_type,
        'items': get_catalog_items(sub_catalog_name, current_item_type),
    }
    return render(request, 'catalog/sub_catalog.html', {**context, **SUB_CATALOG_CONTEXT})


def item(request, item_id, current_catalog):
    CATALOG_TABLES = {'trucks': Truck, 'parts': Part}
    catalog_item = CATALOG_TABLES[current_catalog].objects.get(pk=item_id)
    context = {
        'current_catalog': current_catalog,
        'item': catalog_item,
    }
    return render(request, 'catalog/item.html', {**context, **SUB_CATALOG_CONTEXT})
