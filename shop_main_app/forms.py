from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from shop_main_app.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email адреса / Ім\'я користувача')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'id': 'loginName'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'id': 'loginPassword'})


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'id': 'firstName'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'id': 'lastName'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'id': 'registerEmail'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'id': 'registerPassword'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'id': 'registerRepeatPassword'})

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not first_name.isalpha():
            raise forms.ValidationError('Only letter')

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if not last_name.isalpha():
            raise forms.ValidationError('Only letter')

        return last_name
