from django.shortcuts import render

from home.constants import SECTIONS_DATA, START_PAGE_DATA


def get_section_data(section_name, previous_section):
    return {'section_name': section_name, 'previous_section': previous_section, **SECTIONS_DATA[section_name]}


def start(request):
    return render(request, 'home/home.html', START_PAGE_DATA)


def section(request, section_name, previous_section):
    section_data = get_section_data(section_name, previous_section)
    return render(request, section_data['template'], section_data)
