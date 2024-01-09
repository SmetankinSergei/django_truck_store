from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('sub_catalog/<str:section_name>/<str:previous_section>/<str:sub_catalog_name>/<str:prev_item_type>/',
         views.sub_catalog, name='sub_catalog'),
]
