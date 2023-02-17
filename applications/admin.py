from django.contrib import admin
from django.apps import apps

# Register all applications models.
applications_models = apps.get_app_config("applications").get_models()
for model in applications_models:
    admin.site.register(model)
