from django import template

from catalog.constants import SUB_CATALOGS

register = template.Library()


@register.simple_tag()
def get_sub_catalogs():
    # return SubCatalog.objects.all()
    return SUB_CATALOGS
