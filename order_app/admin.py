from django.contrib import admin
from order_app.forms import OrderItemModelForm
from order_app.formset import OrderItemInlineFormSet
from order_app.models import Order, OrderItem


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 0
    verbose_name = 'Товар'
    verbose_name_plural = 'Товари'
    readonly_fields = ('price', )
    form = OrderItemModelForm
    formset = OrderItemInlineFormSet


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
