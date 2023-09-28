from django.contrib import admin
from orders.forms import OrderItemModelForm

# Register your models here.

from orders.models import Order, OrderItem


class OrderItemAdmin(admin.StackedInline):
    model = OrderItem
    extra = 0
    verbose_name = 'Товар'
    verbose_name_plural = 'Товари'
    readonly_fields = ('price', )
    form = OrderItemModelForm


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemAdmin]
    list_display = ['first_name',
                    'last_name',
                    'email',
                    'phone',
                    'created',
                    'updated',
                    'confirmed',
                    'sent',
                    'paid',
                    'declined'
                    ]

    class Meta:
        model = Order

