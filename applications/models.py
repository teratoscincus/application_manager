from django.contrib.auth.models import User
from django.db import models


class Institute(models.Model):
    name = models.CharField(unique=True, max_length=225)
    url = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return f"({self.pk}) {self.name}"


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    institute = models.ForeignKey(Institute, on_delete=models.PROTECT)
    has_applied = models.BooleanField(default=False)
    deadline = models.DateField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    class Meta:
        unique_together = (
            "title",
            "institute",
        )

    def __str__(self) -> str:
        return f"({self.pk}) {self.title} @ {self.institute}"


class AdmissionTest(models.Model):
    """Admission test linked to an application."""

    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    start = models.DateField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    done = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.application.institute}: {self.application.title} - Done: {self.done}"
