# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from datetime import datetime

from django.shortcuts import get_object_or_404, redirect, render

from .forms import RentsForm, RoomForm, UserDetailsForm
from .models import MONTH_CHOICES, Rent, Room, UserDetails


# Room rent dashboard view
def rent_dashboard(request):
    filter_month = request.GET.get("filter_month", "")
    filter_year = request.GET.get("filter_year", "")

    # Get the available years for filtering
    all_years = Rent.objects.values("paid_date__year").distinct()
    year_choices = [str(year["paid_date__year"]) for year in all_years]

    # Base query for Rent model
    rents = Rent.objects.all()

    # Apply filtering by month
    if filter_month:
        rents = rents.filter(rent_month=filter_month)

    # Apply filtering by year
    if filter_year:
        rents = rents.filter(paid_date__year=filter_year)

    # Calculate the total revenue, total rents, and total overdue rents
    total_revenue = sum(rent.amount for rent in rents)
    total_collected = rents.count()
    overdue_rents = rents.filter(paid_date__lt=datetime.today()).count()

    # Additional statistics
    total_paid_amount = sum(
        rent.amount for rent in rents.filter(paid_date__isnull=False)
    )
    total_pending_amount = total_revenue - total_paid_amount
    average_rent_amount = total_revenue / total_collected if total_collected else 0
    rent_payment_completion_rate = (
        (total_collected / rents.count()) * 100 if rents.count() > 0 else 0
    )
    total_users = rents.values("user").distinct().count()
    total_rooms_rented = rents.values("room_no").distinct().count()

    context = {
        "rents": rents,
        "total_revenue": total_revenue,
        "total_collected": total_collected,
        "total_overdue": overdue_rents,
        "total_paid_amount": total_paid_amount,
        "total_pending_amount": total_pending_amount,
        "average_rent_amount": average_rent_amount,
        "rent_payment_completion_rate": rent_payment_completion_rate,
        "total_users": total_users,
        "total_rooms_rented": total_rooms_rented,
        "filter_month": filter_month,
        "filter_year": filter_year,
        "month_choices": MONTH_CHOICES,
        "year_choices": year_choices,
    }
    return render(request, "admin/rent_dashboard.html", context)


# List View for Rooms
def room_list(request):
    rooms = Room.objects.all()
    return render(request, "admin/room_list.html", {"rooms": rooms})


# Create View for Rooms
def room_create(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("room_list")
    else:
        form = RoomForm()
    return render(request, "admin/room_form.html", {"form": form})


# Update View for Rooms
def room_update(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("room_list")
    else:
        form = RoomForm(instance=room)
    return render(request, "admin/room_form.html", {"form": form})


# Delete View for Rooms
def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        room.delete()
        return redirect("room_list")
    return render(request, "admin/room_confirm_delete.html", {"room": room})


# List View for Rents
def rent_list(request):
    rents = Rent.objects.all()
    month_dict = dict(MONTH_CHOICES)
    for rent in rents:
        rent.rent_month = month_dict.get(rent.rent_month)
    return render(request, "admin/rent_list.html", {"rents": rents})


# Create View for Rents
def rent_create(request):
    if request.method == "POST":
        form = RentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("rent_list")
    else:
        form = RentsForm()
    return render(request, "admin/rent_form.html", {"form": form})


# Update View for Rents
def rent_update(request, pk):
    rent = get_object_or_404(Rent, pk=pk)
    if request.method == "POST":
        form = RentsForm(request.POST, instance=rent)
        if form.is_valid():
            form.save()
            return redirect("rent_list")
    else:
        form = RentsForm(instance=rent)
    return render(request, "admin/rent_form.html", {"form": form})


# Delete View for Rents
def rent_delete(request, pk):
    rent = get_object_or_404(Rent, pk=pk)
    if request.method == "POST":
        rent.delete()
        return redirect("rent_list")
    return render(request, "admin/rent_confirm_delete.html", {"rent": rent})


# List View for UserDetails
def user_details_list(request):
    users = UserDetails.objects.all()
    return render(request, "admin/user_details_list.html", {"users": users})


# Create View for UserDetails
def user_details_create(request):
    if request.method == "POST":
        form = UserDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("user_details_list")
    else:
        form = UserDetailsForm()
    return render(request, "admin/user_details_form.html", {"form": form})


# Update View for UserDetails
def user_details_update(request, pk):
    user = get_object_or_404(UserDetails, pk=pk)
    if request.method == "POST":
        form = UserDetailsForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user_details_list")
    else:
        form = UserDetailsForm(instance=user)
    return render(request, "admin/user_details_form.html", {"form": form})


# Delete View for UserDetails
def user_details_delete(request, pk):
    user = get_object_or_404(UserDetails, pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect("user_details_list")
    return render(request, "admin/user_details_confirm_delete.html", {"user": user})
