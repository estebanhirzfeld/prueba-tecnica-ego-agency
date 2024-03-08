from django.urls import path
from .views import VehicleTypesListView, VehicleTypeRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', VehicleTypesListView.as_view(), name='all-vehicle-types-list'),
    path('<uuid:id>/', VehicleTypeRetrieveUpdateDestroyAPIView.as_view(), name='vehicle-type-detail'),
]
