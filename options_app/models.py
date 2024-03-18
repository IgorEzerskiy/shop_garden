from django.db import models
from django.utils.translation import gettext_lazy as _
from shop_main_app.models import Category
from shop_main_app.validators import ImageValidator
from tinymce.models import HTMLField

CONTACT_FROM_STATUS_CHOICES = (
    (_("processed"), "ОБРОБЛЕНО"),
    (_("awaits"), "ОЧІКУЄ")
)


class ContactForm(models.Model):
    name = models.CharField(_("name"),
                            max_length=40
                            )
    email = models.CharField(_("email address"))
    message = models.TextField(verbose_name='Повідомлення',
                               max_length=500
                               )
    status = models.CharField(verbose_name='Статус',
                              max_length=9,
                              choices=CONTACT_FROM_STATUS_CHOICES,
                              default=_("awaits")
                              )

    class Meta:
        verbose_name = 'Контактна форма'
        verbose_name_plural = 'Запити з "контактної форми"'

    def __str__(self):
        return f'{self.name}/{self.email}'


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


class TextAtMainPage(models.Model):
    main_text = HTMLField(null=True,
                          blank=True,
                          verbose_name='Основний текст'
                          )

    class Meta:
        verbose_name = 'Текст головної сторінки'
        verbose_name_plural = 'Текст сторінки "Головна"'

    def __str__(self):
        return f'Текст головної сторінки'


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
