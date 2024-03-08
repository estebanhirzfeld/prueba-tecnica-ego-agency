from django.contrib import admin
from .models import Brand

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

admin.site.register(Brand, BrandAdmin)