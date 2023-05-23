from django.urls import path

from .views import (
    AdmissionTestsView,
    CreateApplicationView,
    ListApplicationsView,
    UpdateAdmissionTestView,
    UpdateApplicationView,
)

AdmissionTestsView, UpdateAdmissionTestView

app_name = "applications"
urlpatterns = [
    path("", ListApplicationsView.as_view(), name="applications"),
    path("add-application/", CreateApplicationView.as_view(), name="add-application"),
    path(
        "update-application/<int:pk>/",
        UpdateApplicationView.as_view(),
        name="edit-application",
    ),
    path("admission-tests/", AdmissionTestsView.as_view(), name="admission-tests"),
    path(
        "update-admission-test/<int:pk>/",
        UpdateAdmissionTestView.as_view(),
        name="edit-admission-test",
    ),
]
