import json
import os

from django.core.management import BaseCommand

from catalog.models import Part, TruckInfo, Truck, SubCatalog

TABLES_DICT = {'subcatalog': SubCatalog, 'part': Part, 'truckinfo': TruckInfo, 'truck': Truck}
TABLES_DATAFILES = ['sub_catalog_data.json', 'part_data.json', 'truck_info_data.json', 'truck_data.json']


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for table in TABLES_DICT.values():
            table.objects.all().delete()

        for datafile in TABLES_DATAFILES:

            path = os.path.join('datafiles', datafile)

            with open(path) as file:
                tables_data = json.load(file)
                preloading_list = []
                table = None
                for item in tables_data:
                    table = TABLES_DICT[item['model'].split('.')[1]]
                    preloading_list.append(table(**item['fields']))
                table.objects.bulk_create(preloading_list)
