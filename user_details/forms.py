# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

from django import forms

from .models import UserDetails


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "address",
            "photo",
            "aadhaar_card_front_photo",
            "aadhaar_card_back_photo",
        ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.Textarea(attrs={"class": "form-control"}),
            "photo": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "aadhaar_card_front_photo": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
            "aadhaar_card_back_photo": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
        }
