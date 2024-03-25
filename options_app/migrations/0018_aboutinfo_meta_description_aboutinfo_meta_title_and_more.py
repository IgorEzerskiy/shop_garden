# Generated by Django 4.2.4 on 2024-03-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('options_app', '0017_alter_textatmainpage_meta_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutinfo',
            name='meta_description',
            field=models.TextField(blank=True, max_length=160, null=True, verbose_name='Короткий опис'),
        ),
        migrations.AddField(
            model_name='aboutinfo',
            name='meta_title',
            field=models.TextField(blank=True, max_length=60, null=True, verbose_name='Назва сторінки'),
        ),
        migrations.AddField(
            model_name='returnpolicy',
            name='meta_description',
            field=models.TextField(blank=True, max_length=160, null=True, verbose_name='Короткий опис'),
        ),
        migrations.AddField(
            model_name='returnpolicy',
            name='meta_title',
            field=models.TextField(blank=True, max_length=60, null=True, verbose_name='Назва сторінки'),
        ),
        migrations.AddField(
            model_name='shippingandbilling',
            name='meta_description',
            field=models.TextField(blank=True, max_length=160, null=True, verbose_name='Короткий опис'),
        ),
        migrations.AddField(
            model_name='shippingandbilling',
            name='meta_title',
            field=models.TextField(blank=True, max_length=60, null=True, verbose_name='Назва сторінки'),
        ),
    ]
