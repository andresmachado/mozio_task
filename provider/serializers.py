from rest_framework import serializers

from .models import Polygon, Provider


class ProviderSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Provider
        fields = (
            'id',
            'username',
            'user',
            'name',
            'email',
            'phone_number',
            'language',
            'currency'
        )


class PolygonSerializer(serializers.ModelSerializer):
    provider_name = serializers.ReadOnlyField(source='provider.name')

    class Meta:
        model = Polygon
        fields = ('provider', 'provider_name', 'name', 'price', 'poly')
