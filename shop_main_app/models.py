from django.db import models


# Create your models here.


class Measure(models.Model):
    name = models.CharField(verbose_name='Назва')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Назва')
    slug = models.SlugField()
    description = models.TextField(max_length=550, verbose_name='Опис')
    image = models.ImageField(
        upload_to='shop_garden/media/category_images/',
        max_length=100,
        verbose_name='Зображення'
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=256, verbose_name='Назва')
    slug = models.SlugField()
    description = models.TextField(verbose_name='Опис')
    characteristics = models.TextField(verbose_name='Характеристики')
    quantity = models.IntegerField(verbose_name='К-сть')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    availability = models.BooleanField(default=True, verbose_name='Наявність')
    measure = models.ForeignKey(Measure, on_delete=models.DO_NOTHING, related_name='product', verbose_name='Міра')
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, related_name='products', verbose_name='Категорія')
    index = models.BooleanField(default=True)
    discount = models.PositiveIntegerField(default=0, verbose_name='Знижка')
    supplier_discount = models.TextField(max_length=500)

    def __str__(self):
        return f'Товар {self.title}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', verbose_name='Товар')
    image = models.ImageField(upload_to='product_images/', verbose_name='Зображення')
