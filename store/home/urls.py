from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.start, name='start'),
    path('section/<str:section_name>/<str:previous_section>/', views.section, name='section'),
]
