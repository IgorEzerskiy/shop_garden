from django import forms
from django.forms import IntegerField, NumberInput


class CartAddProductForm(forms.Form):
    quantity = IntegerField(widget=NumberInput(attrs={'type': 'number',
                                                      'class': 'form-control-height-lg',
                                                      'value': '0',
                                                      'id': 'cart_quantity',
                                                      'min': '0',
                                                      'placeholder': 'Кількість',
                                                      'name': 'cart_quantity',
                                                      }), label='')

    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)


