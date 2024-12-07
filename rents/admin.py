from django.contrib import admin

from .models import Rent, Room, UserDetails

admin.site.register(Room)
admin.site.register(Rent)
admin.site.register(UserDetails)
