from django import forms
from django.forms import inlineformset_factory
from .models import Order, OrderItem

OrderItemFormSet = inlineformset_factory(
    Order,
    OrderItem,
    fields=['product', 'price', 'quantity'],
    extra=1,
)


class OrderItemInlineFormSet(OrderItemFormSet):
    def clean(self):
        if any(self.errors):
            return

        products_set = set()
        duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                product = form.cleaned_data['product']
                if product in products_set:
                    form.add_error('product', 'Ви не можете додати цей продукт до замовлення, оскільки він вже існує.')
                    duplicates = True
                else:
                    products_set.add(product)

        if duplicates:
            raise forms.ValidationError('У замовленні знайдено дублікати продуктів.')
