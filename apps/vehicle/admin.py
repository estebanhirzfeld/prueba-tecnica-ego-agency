from django.contrib import admin
from .models import Vehicle, VehicleFeature
# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('year', 'brand', 'model', 'price')
    list_filter = ('year', 'brand', 'model', 'type')
    search_fields = ('year', 'brand__name', 'model', 'type__name')

class VehicleFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'vehicle')
    list_filter = ('vehicle',)
    search_fields = ('title', 'description')

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleFeature, VehicleFeatureAdmin)