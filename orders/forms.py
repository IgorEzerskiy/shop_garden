from django.forms import ModelForm, ValidationError
from orders.models import OrderItem


class OrderItemModelForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')

        if quantity > self.cleaned_data.get('product').quantity:
            raise ValidationError('Кількість товару в замовленні більша за його фактичну кількість.')

        return quantity

    def save(self, commit=True):
        instance = super(OrderItemModelForm, self).save(commit=False)

        if not self.cleaned_data.get('price'):
            instance.price = self.cleaned_data.get('product').get_price_with_discount()

        if commit:
            instance.save()

        return instance
