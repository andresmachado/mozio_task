from rest_framework import viewsets

from .models import Polygon, Provider
from .serializers import PolygonSerializer, ProviderSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """API for retrieve, create, update or delete Providers."""
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class PolygonViewSet(viewsets.ModelViewSet):
    """
    API for retrieve, create, update or delete Polygons.

    Returns a list of all polygons in the system.
    """
    serializer_class = PolygonSerializer

    def perform_create(self, serializer):
        serializer.save(provider=self.request.user)

    def get_queryset(self):
        """
        Optionally return polygons results by filtering against a 'lon' and 'lat'
        query parameters in URL.

        Ex: http://localhost:8000/api/polygons/?lon=-10.87890625&lat=52.69636107827448
        """
        queryset = Polygon.objects.all()
        lat = self.request.query_params.get('lat', None)
        lon = self.request.query_params.get('lon', None)
        point = 'POINT({} {})'.format(lon, lat)
        if lat and lon is not None:
            queryset = queryset.filter(poly__contains=point)
        return queryset
