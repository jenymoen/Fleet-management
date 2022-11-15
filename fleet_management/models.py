from email.policy import default
from sre_constants import CATEGORY
from django.db import models
from django.db.models.enums import Choices


# class User(models.Model):
#    first_name = models.CharField(max_length=100, null=True, blank=True)
#    last_name = models.CharField(max_length=100, null=True, blank=True)


class Department(models.Model):
    department_name = models.CharField(max_length=50, null=True, blank=True)

    # def __str__(self):
    #     return self.department_name


class Vehicle(models.Model):

    # VEHICLE_TYPE_CHOICES = ("Varebil Stor", "Varebil Stor")(
    #     "Varebil Liten", "Varebil Liten"
    # )("Personbil Liten", "Personbil Liten")

    # TYRE_TYPE = ("Piggfritt", "Piggfritt")("Pigger", "Pigger")

    reg_number = models.CharField(max_length=7, null=True, unique=True)
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    brand = models.CharField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    vehicle_type = models.CharField(max_length=100, null=True, blank=True)
    build_year = models.IntegerField(null=True, blank=True)
    # bruker = models.ForeignKey(Bruker, null=True, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, default=1, on_delete=models.PROTECT)
    last_km = models.IntegerField(null=True, blank=True)
    date_km = models.DateField(null=True, blank=True)
    winter_tyre = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    tyre_hotel = models.CharField(max_length=100, null=True, blank=True)
    abax_nr = models.CharField(max_length=9, null=True, blank=True)
    last_eu_control = models.DateField(null=True, blank=True)
    next_eu_control = models.DateField(null=True, blank=True)
    vin_number = models.CharField(max_length=100, null=True, blank=True)
    owner = models.CharField(max_length=100, null=True, blank=True)
    leasing_expiry = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.reg_number


class Task(models.Model):

    CATEGORY = (
        ("Service", "Service"),
        ("Tyrechange", "Tyrechange"),
    )

    task_name = models.CharField(max_length=50, null=True, blank=True)
    task_object = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=200, null=True, choices=CATEGORY)
    start_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)

    # Create your models here.
