from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView

from .models import Application


class ListApplicationsView(LoginRequiredMixin, ListView):
    template_name = "applications/applications.html"
    context_object_name = "applications"

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)


class CreateApplicationView(LoginRequiredMixin, CreateView):
    model = Application
    fields = ["title", "school", "applied", "application_deadline", "url"]

    template_name = "applications/new_application.html"
    context_object_name = "form"


class UpdateApplicationView(LoginRequiredMixin, UpdateView):
    model = Application
    fields = ["title", "school", "applied", "application_deadline", "url"]

    template_name = "applications/edit_application.html"
    context_object_name = "form"
