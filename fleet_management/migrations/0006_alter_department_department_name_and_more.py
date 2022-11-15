# Generated by Django 4.1.2 on 2022-11-02 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("fleet_management", "0005_alter_vehicle_department"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="department_name",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="department",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="fleet_management.department",
            ),
        ),
    ]
