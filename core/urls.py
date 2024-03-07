from django.conf import settings
from django.contrib import admin
from django.urls import path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="EGO Motors",
        default_version="v1.0",
        description="EGO Motors endpoints",
        contact=openapi.Contact(email="egomotors@mail.com"), 
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Documentation
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),

    # Admin Panel
    path(settings.ADMIN_URL, admin.site.urls),

]

admin.site.site_header = "EGO Motors Admin"
admin.site.site_title = "EGO Motors Portal"
admin.site.index_title = "Welcome to EGO Motors Portal"