# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from datetime import datetime

from django.shortcuts import redirect, render

from rents.models import MONTH_CHOICES, Rent


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

    # To show month name as string
    month_dict = dict(MONTH_CHOICES)
    for rent in rents:
        rent.rent_month = month_dict.get(rent.rent_month)

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


# Redirect to dashboard view
def redirect_to_dashboard(request):  # pylint: disable=unused-argument
    return redirect(rent_dashboard)
