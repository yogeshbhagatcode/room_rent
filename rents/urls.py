from django.urls import path

from . import views

urlpatterns = [
    # Room URLs
    path("rooms/", views.room_list, name="room_list"),
    path("rooms/create/", views.room_create, name="room_create"),
    path("rooms/<int:pk>/edit/", views.room_update, name="room_update"),
    path("rooms/<int:pk>/delete/", views.room_delete, name="room_delete"),
    # Rent URLs
    path("rents/", views.rent_list, name="rent_list"),
    path("rents/create/", views.rent_create, name="rent_create"),
    path("rents/<int:pk>/edit/", views.rent_update, name="rent_update"),
    path("rents/<int:pk>/delete/", views.rent_delete, name="rent_delete"),
]
