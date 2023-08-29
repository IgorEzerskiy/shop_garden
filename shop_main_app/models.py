from django.db import models


# Create your models here.


class Measure(models.Model):
    name = models.CharField()


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(max_length=550)
    image = models.ImageField(
        upload_to='shop_garden/media/category_images/',
        max_length=100
    )


class Product(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    description = models.TextField()
    characteristics = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    measure = models.ForeignKey(Measure, on_delete=models.DO_NOTHING, related_name='product')
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    images = models.FileField(upload_to='product_images/')
    category = models.ManyToManyField(Category, related_name='products')
    index = models.BooleanField(default=True)
    discount = models.PositiveIntegerField(default=0)
    supplier_discount = models.TextField(max_length=500)
