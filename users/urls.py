"""Define patterns for users."""

from django.urls import path, include

from . import views

app_name = "users"
urlpatterns = [
    path("register/", views.register, name="register"),
    # Include default auth urls.
    path("", include("django.contrib.auth.urls")),
]
