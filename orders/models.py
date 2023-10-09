from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from shop_main_app.models import Product, User

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='orders',
        verbose_name='Корситувач'
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name="Ім'я"
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Прізвище'
    )
    email = models.EmailField(verbose_name='Пошта')
    phone = PhoneNumberField(verbose_name='Номер телефону')
    city = models.CharField(
        max_length=100,
        verbose_name='Місто доставки'
    )
    warehouse = models.CharField(
        max_length=150,
        verbose_name='Відділення'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Створено'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Оновлено'
    )
    confirmed = models.BooleanField(
        default=False,
        verbose_name='Підтверджено'
    )
    sent = models.BooleanField(
        default=False,
        verbose_name='Відправлено'
    )
    paid = models.BooleanField(
        default=False,
        verbose_name='Оплачено'
    )
    declined = models.BooleanField(
        default=False,
        verbose_name='Відмінено'
    )

    class Meta:
        ordering = ['-created', 'confirmed']
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f'Замовлення {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE,
                              verbose_name='Замовлення'
                              )
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE,
                                verbose_name='Продукт'
                                )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Ціна'
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
