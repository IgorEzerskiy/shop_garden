from django.db import models

from shop_main_app.models import Category


# Create your models here.

class Footer(models.Model):
    company_name = models.CharField()
    short_description = models.TextField(max_length=550)
    email = models.EmailField()
    phones = models.TextField()
    facebook = models.CharField()
    instagram = models.CharField()
    viber = models.CharField()
    telegram = models.CharField()
    delivery_info = models.TextField()
    return_conditions = models.TextField()

    class Meta:
        verbose_name = 'Футтер'
        verbose_name_plural = 'Налаштування футтера'

    def __str__(self):
        return f'{self.company_name} footer'


class Carousel(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
    )
    image = models.ImageField(upload_to='carousel/',)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Банери каруселі'
        verbose_name_plural = 'Карусель головної сторінки'

    def __str__(self):
        return f'{self.category.name} banner'
