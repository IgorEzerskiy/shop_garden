from django.db import models

from shop_main_app.models import Category
from shop_main_app.validators import ImageValidator


class ShippingAndBilling(models.Model):
    delivery_info = models.TextField()
    payments = models.TextField()
    extra_context = models.TextField()


class ReturnPolicy(models.Model):
    main_info = models.TextField(null=True, blank=True)
    extra_context = models.TextField()


class Footer(models.Model):
    company_name = models.CharField()
    short_description = models.TextField(max_length=550)
    email = models.EmailField()
    phones = models.TextField()
    facebook = models.CharField(blank=True, null=True)
    instagram = models.CharField(blank=True, null=True)
    viber = models.CharField(blank=True, null=True)
    telegram = models.CharField(blank=True, null=True)

    class Meta:
        verbose_name = 'Футтер'
        verbose_name_plural = 'Налаштування освновного футтера'

    def __str__(self):
        return f'{self.company_name} footer'


class Carousel(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
    )
    image = models.ImageField(
        upload_to='carousel/',
        validators=[ImageValidator(1600, 700)]
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Статус активний/не активний'
    )

    class Meta:
        verbose_name = 'Банери каруселі'
        verbose_name_plural = 'Карусель головної сторінки'

    def __str__(self):
        return f'{self.category.name} banner'
