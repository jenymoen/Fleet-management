from django.urls import path
from fleet_management import views

urlpatterns = [
    path("", views.home, name="home"),
    path("overview/", views.overview, name="overview"),
    path("vehicles_list/", views.vehicles_list, name="vehicles_list"),
    path("create_vehicle/", views.createVehicle, name="create_vehicle"),
    path("edit_vehicle/<str:pk>/", views.editVehicle, name="edit_vehicle"),
    path(
        "vehicle_detailview/<str:pk>/",
        views.detailViewVehicle,
        name="vehicle_detailview",
    ),
    path("create_task/", views.createTask, name="create_task"),
    path("task_list/", views.task_list, name="task_list"),
    path("task_detailview/<str:pk>", views.detailViewTask, name="task_detailview"),
    path("edit_task/<str:pk>/", views.editTask, name="edit_task"),
    path("expense_list/", views.expenseList, name="expense_list"),
    path("create_expense/", views.createExpense, name="create_expense"),
]
