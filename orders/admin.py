from django.contrib import admin
from django.db import transaction
from django.db.models import QuerySet

from orders.forms import OrderItemModelForm
from orders.formset import OrderItemInlineFormSet
from orders.models import Order, OrderItem
from django.contrib import messages

from shop_main_app.models import Product


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
    actions = ('delete_orders', )
    admin.site.disable_action('delete_selected')

    class Meta:
        model = Order

    @admin.action(description='Видалити обрані замовлення')
    def delete_orders(self, request, queryset: QuerySet):
        with transaction.atomic():
            for obj in queryset:
                for order_item in obj.items.all():

                    # 1 method to increase quantity

                    order_item.product.quantity += order_item.quantity
                    order_item.product.save()

                    # # 2 method to increase quantity

                    # product = Product.objects.get(id=order_item.product.id)
                    # product.quantity += order_item.quantity
                    # product.save()

            queryset.delete()
        self.message_user(request, f"удален", messages.SUCCESS)
