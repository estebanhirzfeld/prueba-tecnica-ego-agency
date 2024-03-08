from django.contrib import admin
from .models import Type

# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(Type, TypeAdmin)
