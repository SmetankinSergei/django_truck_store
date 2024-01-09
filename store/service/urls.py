from django.urls import path

from . import views

app_name = 'srvice'

urlpatterns = [
    path('', views.variants, name='variants'),
]
