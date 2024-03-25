from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from shop_main_app.transliterator import transliterate_ua_to_en
from random import randint
from shop_main_app.validators import ImageValidator
from decimal import Decimal
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField
from datetime import datetime, timedelta


class User(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        null=True,
        blank=True
    )
    city = models.CharField(
        max_length=100,
        verbose_name='Місто доставки',
        null=True,
        blank=True
    )
    warehouse = models.CharField(
        max_length=150,
        verbose_name='Відділення',
        null=True,
        blank=True
    )
    first_name = models.CharField(
        _("first name"),
        max_length=150
    )
    last_name = models.CharField(
        _("last name"),
        max_length=150
    )
    email = models.EmailField(
        _("email address"),
        unique=True
    )
    phone = PhoneNumberField(
        verbose_name='Телефон'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Measure(models.Model):
    name = models.CharField(verbose_name='Назва')

    class Meta:
        verbose_name = 'Одиниця виміру'
        verbose_name_plural = 'Одиниці виміру'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Назва'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Слаг',
        max_length=256,
    )
    description = HTMLField(
        max_length=550,
        verbose_name='Опис'
    )
    image = models.ImageField(
        upload_to='category_images/',
        max_length=100,
        verbose_name='Зображення'
    )

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(transliterate_ua_to_en(self.name))}'

        return super().save(**kwargs)

    def get_absolute_url(self):
        return f'/category/{self.slug}'


class Product(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Назва'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Слаг',
        max_length=256,
    )
    description = HTMLField(verbose_name='Опис')
    characteristics = HTMLField(verbose_name='Характеристики')
    quantity = models.PositiveIntegerField(verbose_name='К-сть')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Ціна'
    )
    availability = models.BooleanField(
        default=True,
        verbose_name='Наявність'
    )
    measure = models.ForeignKey(
        Measure,
        on_delete=models.DO_NOTHING,
        related_name='product',
        verbose_name='Міра'
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(
        Category,
        related_name='products',
        verbose_name='Категорія'
    )
    index = models.BooleanField(
        default=True,
        verbose_name='Відбраження на сайті'
    )
    discount = models.PositiveIntegerField(
        default=0,
        verbose_name='Знижка'
    )
    supplier_discount = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='Знижка від постачальника'
    )
    number_of_purchases = models.PositiveIntegerField(
        default=0,
        verbose_name='Кількість покупок товару'
    )
    add_to_popular = models.BooleanField(
        default=False,
        verbose_name='Додати до популярного'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def save(self, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(transliterate_ua_to_en(self.title))}'
        return super().save(**kwargs)

    def __str__(self):
        return f'Товар {self.title}'

    def get_price_with_discount(self):
        return round(self.price - ((self.discount / Decimal(100)) * self.price), 2)

    def is_it_new_product(self) -> bool:
        difference = datetime.now().date() - self.created_at
        if difference < timedelta(days=14):
            return True
        return False

    def get_absolute_url(self):
        return f'/product/{self.slug}'


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Товар'
    )
    image = models.ImageField(
        upload_to='product_images/',
        verbose_name='Зображення',
        validators=[ImageValidator(700, 600)]
    )

    class Meta:
        verbose_name = 'Картинка товару'
        verbose_name_plural = 'Картинки товарів'

    def __str__(self):
        return f'Картинка для товару - {self.product.title}'
