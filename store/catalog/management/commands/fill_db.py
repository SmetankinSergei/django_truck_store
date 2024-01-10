import json
import os

from django.core.management import BaseCommand

from catalog.models import Part, TruckInfo, Truck, SubCatalog

TABLES_LIST = [Part, TruckInfo, Truck, SubCatalog]
TABLES_DATAFILES = ['sub_catalog_data.json', 'part_data.json', 'truck_info_data.json', 'truck_data.json']


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # for table in TABLES_LIST:
        #     table.objects.all().delete()

        for datafile in TABLES_DATAFILES:
            path = os.path.join('datafiles', datafile)

            with open(path) as file:
                tables_data = json.load(file)
                print(type(tables_data))
                print(tables_data)
