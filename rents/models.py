# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

from django.db import models

from user_details.models import UserDetails

MONTH_CHOICES = [
    ("01", "January"),
    ("02", "February"),
    ("03", "March"),
    ("04", "April"),
    ("05", "May"),
    ("06", "June"),
    ("07", "July"),
    ("08", "August"),
    ("09", "September"),
    ("10", "October"),
    ("11", "November"),
    ("12", "December"),
]


class Room(models.Model):
    room_no = models.IntegerField(blank=False, null=False)
    information = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Room no {self.room_no}"


class Rent(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    rent_month = models.CharField(max_length=2, choices=MONTH_CHOICES)
    paid_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        # pylint: disable=no-member
        return f"Rent for {self.room_no} by {self.user.get_username()}"
