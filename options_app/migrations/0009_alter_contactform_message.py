# Generated by Django 4.2.4 on 2024-01-22 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('options_app', '0008_contactform_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='message',
            field=models.TextField(max_length=500, verbose_name='message'),
        ),
    ]
