# Generated by Django 4.2.4 on 2023-10-15 12:23

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('options_app', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='returnpolicy',
            name='extra_context',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='returnpolicy',
            name='main_info',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shippingandbilling',
            name='delivery_info',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='shippingandbilling',
            name='extra_context',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='shippingandbilling',
            name='payments',
            field=tinymce.models.HTMLField(),
        ),
    ]