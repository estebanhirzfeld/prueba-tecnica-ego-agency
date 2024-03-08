from django.db import models
from apps.common.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from apps.vehicle_brand.models import Brand
from apps.vehicle_type.models import Type

# Create your models here.
class Vehicle(TimeStampedModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name=_('Brand'), related_name='vehicles')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name=_('Vehicle Type'))
    model = models.CharField(verbose_name=_('Model'), max_length=100)
    year = models.PositiveIntegerField(verbose_name=_('Year'))
    price = models.DecimalField(verbose_name=_('Price'), max_digits=15, decimal_places=0)
    image = models.ImageField(verbose_name=_('Image'), upload_to='images/vehicles', blank=True, null=True)
    heading_title = models.CharField(verbose_name=_('Heading Title'), max_length=255, blank=True, null=True)
    heading_description = models.TextField(verbose_name=_('Heading Description'), blank=True, null=True)

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"
    
class VehicleFeature(TimeStampedModel):
    vehicle = models.ForeignKey(Vehicle, related_name='features', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='vehicle_features/')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
