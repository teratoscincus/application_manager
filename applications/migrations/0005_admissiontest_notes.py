# Generated by Django 4.1.7 on 2023-04-13 11:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("applications", "0004_admissiontest_start"),
    ]

    operations = [
        migrations.AddField(
            model_name="admissiontest",
            name="notes",
            field=models.TextField(blank=True),
        ),
    ]