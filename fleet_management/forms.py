from django import forms
from django.forms.widgets import DateInput
from fleet_management.models import *
from django.forms import ModelForm


class DateInput(forms.DateInput):
    input_type = "date"


class DateForm(forms.Form):
    date = forms.DateField(widget=DateInput)


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
        widgets = {
            "date_km": DateInput(),
            "next_eu_control": DateInput(),
            "leasing_expiry": DateInput(),
        }


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
        widgets = {"start_date": DateInput(), "due_date": DateInput()}


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = [
            "exp_date",
            "expense_category",
            "amount",
        ]

        widgets = {"exp_date": DateInput()}
