from django import template

from home.constants import SITE_SECTIONS

register = template.Library()


@register.simple_tag()
def get_sections():
    return SITE_SECTIONS
