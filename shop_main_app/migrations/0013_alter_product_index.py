# Generated by Django 4.2.4 on 2023-09-17 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_main_app', '0012_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='index',
            field=models.BooleanField(default=True, verbose_name='Відбраження на сайті'),
        ),
    ]