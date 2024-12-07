from django.urls import path

from . import views

urlpatterns = [
    # Dashboard URLs
    path("", views.redirect_to_dashboard, name="redirect_to_dashboard"),
    path("dashboard/", views.rent_dashboard, name="rent_dashboard"),
]
