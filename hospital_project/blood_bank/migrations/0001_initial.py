# Generated by Django 5.0.1 on 2024-01-29 06:13

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BloodInventory",
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
                ("blood_group", models.CharField(max_length=2)),
                ("quantity_liters", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
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
                ("name", models.CharField(max_length=255)),
                ("blood_group", models.CharField(max_length=2)),
                ("blood_required_liters", models.IntegerField()),
                ("days_in_hospital", models.IntegerField()),
            ],
        ),
    ]
