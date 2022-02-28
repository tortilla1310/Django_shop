import hashlib
import os
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import ModelForm, forms
from django import forms

from .models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = (
            "username",
            "first_name",
            "password1",
            "password2",
            "email",
            "age",
            "avatar",
            "city",
            "phone",
        )

    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    def save(self):
        user = super().save()
        user.is_active = False
        user.activation_key = hashlib.md5(
            user.email.encode('utf-8') + os.urandom(16)).hexdigest()
        user.save()
        return user


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = (
            "username",
            "first_name",
            "password",
            "email",
            "age",
            "avatar",
            "city",
            "phone",
        )

    def __init__(self, *args, **kwargs):
        super(ShopUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            if field_name == "password":
                field.widget = forms.HiddenInput()


def clean_city(self):
    city = self.cleaned_data['city']
    if city == 'Moscow':
        raise forms.ValidationError("The shop in Moscow is closed.")
    return city
