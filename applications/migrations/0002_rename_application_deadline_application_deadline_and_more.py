# Generated by Django 4.1.7 on 2023-02-17 12:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("applications", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="application",
            old_name="application_deadline",
            new_name="deadline",
        ),
        migrations.RenameField(
            model_name="application",
            old_name="applied",
            new_name="has_applied",
        ),
    ]
