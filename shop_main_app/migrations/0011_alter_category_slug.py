# Generated by Django 4.2.4 on 2024-03-20 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_main_app', '0010_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=256, unique=True, verbose_name='Слаг'),
        ),
    ]
