from django.shortcuts import render
from rest_framework import generics
from .models import Type 
from .serializers import TypeSerializer 

# Create your views here.
class VehicleTypesListView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class VehicleTypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    lookup_field = 'id'