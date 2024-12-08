# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserDetails(AbstractUser):
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    aadhaar_card_front_photo = models.ImageField(
        upload_to="aadhaar_card_front_pics/", blank=True, null=True
    )
    aadhaar_card_back_photo = models.ImageField(
        upload_to="aadhaar_card_back_pics/", blank=True, null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}"
