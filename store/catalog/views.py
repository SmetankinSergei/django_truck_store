from django.core.paginator import Paginator
from django.shortcuts import render

from catalog.constants import ITEMS_TYPES_DATA, SUB_CATALOG_CONTEXT, SUB_CATALOG_TEMPLATES
from catalog.models import Truck, Part
from catalog.templatetags.catalog_tags import get_catalog_items


def catalog(request):
    return render(request, 'catalog/catalog.html')


def sub_catalog(request, sub_catalog_name, current_item_type, prev_item_type):
    # current_item_type = request.GET.get('current_item_type', 'all types')
    # prev_item_type = request.GET.get('prev_item_type', 'all types')

    items = get_catalog_items(sub_catalog_name, current_item_type)
    # paginator = Paginator(items, 6)
    # current_page = paginator.page(1)

    context = {
        'sub_catalog_name': sub_catalog_name,
        'types_data': ITEMS_TYPES_DATA[sub_catalog_name],
        'current_item_type': current_item_type,
        'prev_item_type': prev_item_type,
        'items': items,
    }
    return render(request, 'catalog/sub_catalog.html', {**context, **SUB_CATALOG_CONTEXT})


def item(request, item_id, sub_catalog_name):
    CATALOG_TABLES = {'trucks': Truck, 'parts': Part}
    catalog_item = CATALOG_TABLES[sub_catalog_name].objects.get(pk=item_id)
    context = {
        'item': catalog_item,
    }
    return render(request, SUB_CATALOG_TEMPLATES[sub_catalog_name], {**context, **SUB_CATALOG_CONTEXT})
