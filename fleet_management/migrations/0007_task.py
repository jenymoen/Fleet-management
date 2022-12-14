# Generated by Django 4.1.2 on 2022-11-03 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("fleet_management", "0006_alter_department_department_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("task_name", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "task_type",
                    models.CharField(
                        choices=[("Service", "Service"), ("Tyrechange", "Tyrechange")],
                        max_length=200,
                        null=True,
                    ),
                ),
                ("start_date", models.DateField(blank=True, null=True)),
                ("due_date", models.DateField(blank=True, null=True)),
                (
                    "task_object",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fleet_management.vehicle",
                    ),
                ),
            ],
        ),
    ]
