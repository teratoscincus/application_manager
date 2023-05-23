from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView, ListView, UpdateView

from .models import AdmissionTest, Application


class ListApplicationsView(LoginRequiredMixin, ListView):
    template_name = "applications/applications.html"
    context_object_name = "applications"

    def get_queryset(self):
        not_applied = (
            Application.objects.filter(user=self.request.user)
            .filter(has_applied=False)
            .order_by("deadline")
        )
        has_applied = (
            Application.objects.filter(user=self.request.user)
            .filter(has_applied=True)
            .order_by("title")
            .order_by("institute__name")
        )

        return {"not_applied": not_applied, "has_applied": has_applied}


class CreateApplicationView(LoginRequiredMixin, CreateView):
    model = Application
    fields = [
        "has_applied",
        "title",
        "institute",
        "deadline",
        "url",
    ]

    template_name = "applications/new_course_application.html"
    context_object_name = "form"
    success_url = "/applications/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateApplicationView(LoginRequiredMixin, UpdateView):
    model = Application
    fields = [
        "has_applied",
        "title",
        "institute",
        "deadline",
        "url",
    ]

    template_name = "applications/edit_course_application.html"
    context_object_name = "form"
    success_url = "/applications/"


class AdmissionTestsView(LoginRequiredMixin, ListView):
    template_name = "applications/admission_tests.html"
    context_object_name = "admission_tests"

    def get_queryset(self):
        """Separate admisson tests where the start date is TBA."""
        tba = AdmissionTest.objects.filter(start=None).order_by(
            "application__institute__name"
        )
        not_done = (
            AdmissionTest.objects.filter(~Q(start=None))
            .filter(done=False)
            .order_by("start")
        )
        is_done = AdmissionTest.objects.filter(done=True).order_by("-start")

        return {"tba": tba, "not_done": not_done, "is_done": is_done}


class UpdateAdmissionTestView(LoginRequiredMixin, UpdateView):
    model = AdmissionTest
    fields = [
        "done",
        "start",
        "deadline",
        "notes",
    ]

    template_name = "applications/edit_admission_test.html"
    context_object_name = "form"
    success_url = "/applications/admission-tests/"
