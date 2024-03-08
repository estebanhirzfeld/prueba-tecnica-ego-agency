from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class VehicleBrandConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.vehicle_brand"
    verbose_name = _("Vehicle Brand")
