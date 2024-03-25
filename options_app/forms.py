from django.forms import ModelForm
from django import forms

from options_app.models import ContactForm
import re


class ContactModelForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name',
                  'email',
                  'message')

    def __init__(self, *args, **kwargs):
        self.product_name = None
        if 'request' in kwargs:
            self.request = kwargs.pop('request')
            self.product_name = self.request.POST.get('product-id')

        super(ContactModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control',
                                                 'id': 'name'})
        self.fields['message'].widget.attrs.update({'class': 'form-control',
                                                    'id': 'message'})
        self.fields['email'].widget.attrs.update({'class': 'form-control',
                                                  'id': 'email'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(pattern, email):
            raise forms.ValidationError('Введіть правильну електронну адресу.')
        return email

    def clean_message(self):
        msg = self.cleaned_data.get('message')

        if self.product_name is not None:
            msg = msg + '\nНазва товару:\n' + self.product_name

        return msg
