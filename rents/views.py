# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from django.shortcuts import get_object_or_404, redirect, render

from .forms import RentsForm, RoomForm
from .models import MONTH_CHOICES, Rent, Room


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
