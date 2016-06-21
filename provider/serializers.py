from rest_framework import serializers

from .models import Polygon, Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = (
            'id',
            'name',
            'email',
            'phone_number',
            'language',
            'currency'
        )


class PolygonSerializer(serializers.ModelSerializer):
    provider = serializers.ReadOnlyField(source='provider.name')

    class Meta:
        model = Polygon
        fields = ('provider', 'name', 'price', 'poly')
