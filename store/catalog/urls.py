from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('sub_catalog/<str:section_name>/<str:previous_section>/<str:sub_catalog_name>/<str:prev_item_type>/',
         views.sub_catalog, name='sub_catalog'),
    path('show_sub_catalog_by_type/<str:sub_catalog_name>/<str:item_type>/<str:prev_item_type>/',
         views.show_sub_catalog_by_type, name='show_sub_catalog_by_type'),
    path('item/<int:item_id>/<str:current_catalog>/', views.item, name='item'),
]
