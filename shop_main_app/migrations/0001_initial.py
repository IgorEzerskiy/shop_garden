# Generated by Django 4.2.4 on 2023-08-29 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('description', models.TextField(max_length=550)),
                ('image', models.ImageField(upload_to='shop_garden/media/category_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('characteristics', models.TextField()),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('availability', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('images', models.FileField(upload_to='product_images/')),
                ('index', models.BooleanField(default=True)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('supplier_discount', models.TextField(max_length=500)),
                ('category', models.ManyToManyField(related_name='products', to='shop_main_app.category')),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='product', to='shop_main_app.measure')),
            ],
        ),
    ]
