# Generated by Django 4.2.4 on 2024-01-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('options_app', '0007_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='status',
            field=models.CharField(choices=[('processed', 'PROCESSED'), ('awaits', 'AWAITS')], default='processed', max_length=9),
        ),
    ]