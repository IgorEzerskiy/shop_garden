# Generated by Django 4.2.4 on 2024-01-18 12:29

from django.db import migrations, models
import django.db.models.deletion
import shop_main_app.validators
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_main_app', '0007_user_city_user_warehouse'),
        ('options_app', '0005_aboutinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutinfo',
            name='left_side_of_page',
            field=tinymce.models.HTMLField(verbose_name='Ліва частина сторінки'),
        ),
        migrations.AlterField(
            model_name='aboutinfo',
            name='right_side_of_page',
            field=tinymce.models.HTMLField(verbose_name='Права частина сторінки'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop_main_app.category', verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(upload_to='carousel/', validators=[shop_main_app.validators.ImageValidator(1600, 700)], verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='company_name',
            field=models.CharField(verbose_name='Назва компанії'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Електронна пошта'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='facebook',
            field=models.CharField(blank=True, null=True, verbose_name='Посилання на Facebook'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='instagram',
            field=models.CharField(blank=True, null=True, verbose_name='Посилання на Instagram'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='phones',
            field=models.TextField(verbose_name='Номери телефонів'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='short_description',
            field=models.TextField(max_length=550, verbose_name='Короткий опис'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='telegram',
            field=models.CharField(blank=True, null=True, verbose_name='Посилання на Telegram'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='viber',
            field=models.CharField(blank=True, null=True, verbose_name='Посилання на Viber'),
        ),
        migrations.AlterField(
            model_name='returnpolicy',
            name='main_info',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Основна інформація'),
        ),
        migrations.AlterField(
            model_name='shippingandbilling',
            name='delivery_info',
            field=tinymce.models.HTMLField(verbose_name='Доставка'),
        ),
        migrations.AlterField(
            model_name='shippingandbilling',
            name='payments',
            field=tinymce.models.HTMLField(verbose_name='Оплата'),
        ),
    ]
