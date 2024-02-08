from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
