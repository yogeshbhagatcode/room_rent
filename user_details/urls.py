from django.urls import path

from . import views

urlpatterns = [
    # User Details URLs
    path("users/", views.user_details_list, name="user_details_list"),
    path("users/create/", views.user_details_create, name="user_details_create"),
    path("users/<int:pk>/edit/", views.user_details_update, name="user_details_update"),
    path(
        "users/<int:pk>/delete/", views.user_details_delete, name="user_details_delete"
    ),
]
