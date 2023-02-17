from django.urls import path

from .views import (
    ListApplicationsView,
    CreateApplicationView,
    UpdateApplicationView,
)

app_name = "applications"
urlpatterns = [
    path("applications/", ListApplicationsView.as_view(), name="applications"),
    path("add-application/", CreateApplicationView.as_view(), name="add-application"),
    path(
        "update-application/", UpdateApplicationView.as_view(), name="edit-application"
    ),
]
