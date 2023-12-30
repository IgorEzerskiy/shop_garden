from django.contrib import admin
from django.db import transaction
from django.db.models import QuerySet

from orders.forms import OrderItemModelForm
from orders.formset import OrderItemInlineFormSet
from orders.models import Order, OrderItem
from django.contrib import messages


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 0
    verbose_name = 'Товар'
    verbose_name_plural = 'Товари'
    readonly_fields = ('price',)
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
    actions = ('delete_orders', 'change_status_confirmed', 'change_status_sent', 'change_status_paid',
               'change_status_declined')
    admin.site.disable_action('delete_selected', )

    class Meta:
        model = Order

    @admin.action(description='Видалити обрані замовлення')
    def delete_orders(self, request, queryset: QuerySet):
        with transaction.atomic():
            for obj in queryset:
                for order_item in obj.items.all():
                    order_item.product.quantity += order_item.quantity
                    order_item.product.save()
            queryset.delete()
        self.message_user(request, f"Успішне видалення", messages.SUCCESS)

    def delete_model(self, request, obj):
        obj.delete()

    @admin.action(description='Статус "Підтвержено" ')
    def change_status_confirmed(self, request, queryset: QuerySet):
        queryset.update(confirmed=True)
        self.message_user(request, f"Статус змінений", messages.SUCCESS)

    @admin.action(description='Статус "Відправлено"')
    def change_status_sent(self, request, queryset: QuerySet):
        queryset.update(sent=True)
        self.message_user(request, f"Статус змінений", messages.SUCCESS)

    @admin.action(description='Статус "Оплачено"')
    def change_status_paid(self, request, queryset: QuerySet):
        queryset.update(paid=True)
        self.message_user(request, f"Статус змінений", messages.SUCCESS)

    @admin.action(description='Статус "Відмінено"')
    def change_status_declined(self, request, queryset: QuerySet):
        queryset.update(declined=True)
        self.message_user(request, f"Статус змінений", messages.SUCCESS)
