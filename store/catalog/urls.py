from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('sub_catalog/<str:sub_catalog_name>/<str:current_item_type>/<str:prev_item_type>/',
         views.sub_catalog, name='sub_catalog'),
    path('item/<int:item_id>/<str:sub_catalog_name>/', views.item, name='item'),
]
