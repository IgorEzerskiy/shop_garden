from django.forms import ModelForm, ValidationError
from orders.models import OrderItem, Order


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


class OrderCreateForm(ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'warehouse']

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['warehouse'].widget.attrs.update({'class': 'form-control'})

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not first_name.isalpha():
            raise ValidationError('Only letter')

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if not last_name.isalpha():
            raise ValidationError('Only letter')

        return last_name
