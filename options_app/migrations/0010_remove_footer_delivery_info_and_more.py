# Generated by Django 4.2.4 on 2023-09-15 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('options_app', '0009_returnpolicy_main_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='delivery_info',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='return_conditions',
        ),
        migrations.AlterField(
            model_name='footer',
            name='facebook',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='footer',
            name='instagram',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='footer',
            name='telegram',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='footer',
            name='viber',
            field=models.CharField(blank=True, null=True),
        ),
    ]
