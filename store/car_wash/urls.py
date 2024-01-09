from django.urls import path

from . import views

app_name = 'car_wash'

urlpatterns = [
    path('', views.car_wash, name='car_wash'),
]
