from django.shortcuts import render

from catalog.constants import ITEMS_TYPES_DATA


def catalog(request):
    return render(request, 'catalog/catalog.html')


def sub_catalog(request, section_name, previous_section, sub_catalog_name, prev_item_type):
    page_data = {
        'title': 'MAN - Catalog',
        'section_name': section_name,
        'previous_section': previous_section,
        'sub_catalog_name': sub_catalog_name,
        'is_sub_section': True,
        'types_data': ITEMS_TYPES_DATA[sub_catalog_name],
        'prev_item_type': prev_item_type,
    }
    return render(request, 'catalog/sub_catalog.html', page_data)
