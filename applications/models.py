from django.db import models
from django.contrib.auth.models import User


class Institute(models.Model):
    name = models.CharField(unique=True, max_length=225)
    url = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return f"({self.pk}) {self.name}"


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    institute = models.ForeignKey(Institute, on_delete=models.PROTECT)
    applied = models.BooleanField(default=False)
    application_deadline = models.DateField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    class Meta:
        unique_together = (
            "title",
            "institute",
        )

    def __str__(self) -> str:
        return f"({self.pk}) {self.title} @ {self.institute}"
