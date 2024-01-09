from django.db import models


class SubCatalog(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    label = models.CharField(max_length=20, verbose_name='Label')
    img = models.ImageField(upload_to='sub_catalogs_back_img')

    class Meta:
        verbose_name = 'Sub catalog'
        verbose_name_plural = 'Sub catalogs'
