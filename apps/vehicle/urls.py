from django.urls import path
from .views import VehicleListView, VehicleCreateView ,VehicleRetrieveUpdateDestroyAPIView, VehicleFeatureListCreateView, VehicleFeatureRetrieveUpdateDestroy

urlpatterns = [
    path('', VehicleListView.as_view(), name='vehicle-list'),
    path('create/', VehicleCreateView.as_view(), name='vehicle-create'),
    path('<uuid:id>/', VehicleRetrieveUpdateDestroyAPIView.as_view(), name='vehicle-detail'),

    path('features/<uuid:id>/', VehicleFeatureListCreateView.as_view(), name='vehicle-feature-list-create'),
    path('feature/<uuid:id>/', VehicleFeatureRetrieveUpdateDestroy.as_view(), name='vehicle-feature-retrieve-update-destroy'),
]