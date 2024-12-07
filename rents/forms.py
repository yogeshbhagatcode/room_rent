# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

from django import forms

from .models import Rent, Room, UserDetails


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["room_no", "information"]
        widgets = {
            "room_no": forms.NumberInput(attrs={"class": "form-control"}),
            "information": forms.TextInput(attrs={"class": "form-control"}),
        }


class RentsForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ["user", "room_no", "amount", "rent_month", "paid_date"]
        widgets = {
            "user": forms.Select(attrs={"class": "form-control"}),
            "room_no": forms.Select(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "rent_month": forms.Select(attrs={"class": "form-control"}),
            "paid_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }


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
        ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.Textarea(attrs={"class": "form-control"}),
            "photo": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
