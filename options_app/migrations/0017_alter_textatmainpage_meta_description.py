# Generated by Django 4.2.4 on 2024-03-25 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('options_app', '0016_alter_textatmainpage_meta_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textatmainpage',
            name='meta_description',
            field=models.TextField(blank=True, max_length=160, null=True, verbose_name='Короткий опис'),
        ),
    ]
