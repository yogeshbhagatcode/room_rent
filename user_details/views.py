# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from django.shortcuts import get_object_or_404, redirect, render

from .forms import UserDetailsForm
from .models import UserDetails


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
