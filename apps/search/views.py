from rest_framework.views import APIView
from rest_framework.response import Response
from apps.vehicle.models import Vehicle
from apps.vehicle.serializers import VehicleSerializer


class SearchView(APIView):
    def get(self, request):
        brand_name = request.query_params.get('brand')
        type_name = request.query_params.get('type')
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        newest_first = request.query_params.get('newest_first')
        oldest_first = request.query_params.get('oldest_first')

        vehicles = Vehicle.objects.all()

        if brand_name:
            vehicles = vehicles.filter(brand__name__icontains=brand_name)

        if type_name:
            vehicles = vehicles.filter(type__name__icontains=type_name)

        if min_price:
            vehicles = vehicles.filter(price__gte=min_price)

        if max_price:
            vehicles = vehicles.filter(price__lte=max_price)

        if newest_first:
            vehicles = vehicles.order_by('-year')

        if oldest_first:
            vehicles = vehicles.order_by('year')

        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)
