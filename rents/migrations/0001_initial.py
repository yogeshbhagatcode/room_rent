# Generated by Django 5.1.4 on 2024-12-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Rents",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "rent_month",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=2,
                    ),
                ),
                ("paid_date", models.DateField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("room_no", models.IntegerField()),
                ("information", models.CharField(max_length=200)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
