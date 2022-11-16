# Generated by Django 4.1.2 on 2022-11-15 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fleet_management", "0007_task"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contract",
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
                (
                    "contract_name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Expense",
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
                ("exp_date", models.DateField(blank=True, null=True)),
                (
                    "expense_category",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Spareparts", "Spareparts"),
                            ("Tyres", "Tyres"),
                            ("Gas", "Gas"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                ("amount", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
