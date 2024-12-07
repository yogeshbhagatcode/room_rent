# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

from django import forms

from .models import Rent, Room


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
