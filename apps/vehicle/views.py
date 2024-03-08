from django.shortcuts import render, get_object_or_404
from .models import Vehicle, VehicleFeature
from .pagination import VehiclePagination
from .serializers import VehicleSerializer, VehicleCreateSerializer ,VehicleDetailsSerializer, VehicleFeatureSerializer
from .renderers import VehiclesJSONRenderer
from rest_framework.response import Response
from rest_framework import generics, permissions
# from rest_framework.renderers import BrowsableAPIRenderer


# Create your views here.
class VehicleListView(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VehicleSerializer
    pagination_class = VehiclePagination
    renderer_classes = [VehiclesJSONRenderer]

class VehicleCreateView(generics.CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleCreateSerializer

class VehicleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleDetailsSerializer
    lookup_field = 'id'


class VehicleFeatureListCreateView(generics.ListCreateAPIView):
    queryset = VehicleFeature.objects.all()
    serializer_class = VehicleFeatureSerializer

    def get_queryset(self):
        vehicle_id = self.kwargs.get('id')
        vehicle = get_object_or_404(Vehicle, id=vehicle_id)
        return vehicle.features.all()

    def post(self, request, *args, **kwargs):
        vehicle_id = self.kwargs.get('id')
        vehicle = get_object_or_404(Vehicle, id=vehicle_id)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(vehicle=vehicle)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class VehicleFeatureRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehicleFeature.objects.all()
    serializer_class = VehicleFeatureSerializer

    def get_object(self):
        feature_id = self.kwargs.get('id')
        return get_object_or_404(VehicleFeature, id=feature_id)