from django import forms

from fleet_management.models import Task, Vehicle
from django.forms import ModelForm


class VehiclesForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            "reg_number",
            "brand",
            "model",
            "vehicle_type",
            "build_year",
            "department",
            "last_km",
            "date_km",
            "winter_tyre",
            "tyre_hotel",
            "abax_nr",
            "next_eu_control",
            "vin_number",
            "leasing_expiry",
        ]


class Create_taskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "task_name",
            "task_object",
            "task_type",
            "start_date",
            "due_date",
        ]
