# Generated by Django 4.2.4 on 2023-10-08 17:28

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name="Ім'я")),
                ('last_name', models.CharField(max_length=50, verbose_name='Прізвище')),
                ('email', models.EmailField(max_length=254, verbose_name='Пошта')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер телефону')),
                ('city', models.CharField(max_length=100, verbose_name='Місто доставки')),
                ('warehouse', models.CharField(max_length=150, verbose_name='Відділення')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Оновлено')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Підтверджено')),
                ('sent', models.BooleanField(default=False, verbose_name='Відправлено')),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('declined', models.BooleanField(default=False, verbose_name='Відмінено')),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
                'ordering': ['-created', 'confirmed'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order', verbose_name='Замовлення')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
            },
        ),
    ]
