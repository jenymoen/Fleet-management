import re
from django.utils.timezone import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def home(request):
    return HttpResponse("Hello, Jens Nymoen")


def overview(request):

    name = "Balle"
    now = datetime.now

    return render(request, "fleet_management/overview.html", {"name": name, "now": now})


def vehicles_list(request):
    vehicles = Vehicle.objects.all()

    return render(
        request, "fleet_management/vehicles_list.html", {"vehicles": vehicles}
    )


def createVehicle(request):

    form = VehiclesForm()
    if request.method == "POST":
        form = VehiclesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/vehicles_list/")

    context = {"form": form}

    return render(request, "fleet_management/register_vehicle.html", context)


def editVehicle(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    form = VehiclesForm(instance=vehicle)
    if request.method == "POST":
        form = VehiclesForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect("/vehicles_list/")

    return render(request, "fleet_management/register_vehicle.html", {"form": form})


def detailViewVehicle(request, pk):
    vehicle_detailview = Vehicle.objects.get(id=pk)
    vehicles = Vehicle.objects.all()
    task_vehicle = Task.objects.get(id=pk)
    context = {
        "vehicle_detailview": vehicle_detailview,
        "vehicles": vehicles,
        "task_vehicle": task_vehicle,
    }

    return render(request, "fleet_management/vehicle_detailview.html", context)


def task_list(request):

    tasks = Task.objects.all()

    return render(request, "fleet_management/task_list.html", {"tasks": tasks})


def createTask(request):

    form = Create_taskForm()
    if request.method == "POST":
        form = Create_taskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/vehicles_list/")

    context = {"form": form}

    return render(request, "fleet_management/create_task.html", context)


# Create your views here.
