# Generated by Django 4.1.7 on 2023-04-13 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "applications",
            "0002_rename_application_deadline_application_deadline_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="AdmissionTest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deadline", models.DateField(blank=True, null=True)),
                ("done", models.BooleanField(default=False)),
                (
                    "application",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="applications.application",
                    ),
                ),
            ],
        ),
    ]
