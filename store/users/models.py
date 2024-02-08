from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=250, unique=True)
    avatar = models.ImageField(upload_to='users/avatars/')
    phone = models.CharField(max_length=35, **NULLABLE)
    country = models.CharField(max_length=50, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
