from django.db import models

from shop_main_app.models import Category
from shop_main_app.validators import ImageValidator
from tinymce.models import HTMLField


class ShippingAndBilling(models.Model):
    delivery_info = HTMLField(verbose_name='Доставка')
    payments = HTMLField(verbose_name='Оплата')

    class Meta:
        verbose_name = 'Оплата та доставка'
        verbose_name_plural = 'Текст сторінки "Оплата та доставка"'

    def __str__(self):
        return f'Сторінка "Умови повернення"'


class ReturnPolicy(models.Model):
    main_info = HTMLField(null=True,
                          blank=True,
                          verbose_name='Основна інформація'
                          )

    class Meta:
        verbose_name = 'Умови повернення'
        verbose_name_plural = 'Текст сторінки "Умови повернення"'

    def __str__(self):
        return f'Сторінка "Умови повернення"'


class AboutInfo(models.Model):
    left_side_of_page = HTMLField(verbose_name='Ліва частина сторінки')
    right_side_of_page = HTMLField(verbose_name='Права частина сторінки')

    class Meta:
        verbose_name = 'Про нас'
        verbose_name_plural = 'Текст сторінки "Про нас"'

    def __str__(self):
        return f'Сторінка "Про нас"'


class Footer(models.Model):
    company_name = models.CharField(verbose_name='Назва компанії')
    short_description = models.TextField(max_length=550,
                                         verbose_name='Короткий опис'
                                         )
    email = models.EmailField(verbose_name='Електронна пошта')
    phones = models.TextField(verbose_name='Номери телефонів')
    facebook = models.CharField(blank=True,
                                null=True,
                                verbose_name='Посилання на Facebook'
                                )
    instagram = models.CharField(blank=True,
                                 null=True,
                                 verbose_name='Посилання на Instagram'
                                 )
    viber = models.CharField(blank=True,
                             null=True,
                             verbose_name='Посилання на Viber'
                             )
    telegram = models.CharField(blank=True,
                                null=True,
                                verbose_name='Посилання на Telegram'
                                )

    class Meta:
        verbose_name = 'Футтер'
        verbose_name_plural = 'Налаштування освновного футтера'

    def __str__(self):
        return f'{self.company_name} footer'


class Carousel(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name='Категорія'
    )
    image = models.ImageField(
        upload_to='carousel/',
        validators=[ImageValidator(1600, 700)],
        verbose_name='Картинка'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Статус активний/не активний'
    )

    class Meta:
        verbose_name = 'Банери каруселі'
        verbose_name_plural = 'Карусель головної сторінки'

    def __str__(self):
        return f'{self.category.name} баннер'
