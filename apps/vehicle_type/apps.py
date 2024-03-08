from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class VehicleTypeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.vehicle_type"
    verbose_name = _("Vehicle Type")
