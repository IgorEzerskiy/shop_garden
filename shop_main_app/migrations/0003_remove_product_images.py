# Generated by Django 4.2.4 on 2023-08-29 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_main_app', '0002_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
    ]
