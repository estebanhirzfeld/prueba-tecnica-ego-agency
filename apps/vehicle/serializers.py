from rest_framework import serializers
from .models import Vehicle, VehicleFeature
from apps.vehicle_brand.models import Brand
from apps.vehicle_type.models import Type
from apps.vehicle_type.serializers import TypeSerializer
from apps.vehicle_brand.serializers import BrandSerializer


class VehicleSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()
    class Meta:
        model = Vehicle
        fields = [
            'id',
            'year',
            'brand',
            'price',
        ]

    def get_brand(self, obj):
        return obj.brand.name
    
class VehicleCreateSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    type = TypeSerializer()

    class Meta:
        model = Vehicle
        fields = ['brand', 'type', 'model', 'year', 'price', 'image', 'heading_title', 'heading_description']

    def create(self, validated_data):
        brand_data = validated_data.pop('brand')
        type_data = validated_data.pop('type')

        brand_instance, _ = Brand.objects.get_or_create(**brand_data)
        type_instance, _ = Type.objects.get_or_create(**type_data)

        vehicle = Vehicle.objects.create(brand=brand_instance, type=type_instance, **validated_data)
        return vehicle

class VehicleFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleFeature
        fields = [
            'id',
            'vehicle',
            'img',
            'title',
            'description'
        ]

class VehicleDetailsSerializer(serializers.ModelSerializer):
    features = VehicleFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Vehicle
        fields = [
            'id',
            'brand',
            'model',
            'year',
            'heading_title',
            'heading_description',
            'price',
            'features',
        ]
