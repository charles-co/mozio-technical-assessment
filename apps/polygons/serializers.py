from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Polygon


class PolygonCreateSerializer(GeoFeatureModelSerializer):

    name = serializers.CharField(source="provider.name", read_only=True)

    class Meta:
        model = Polygon
        geo_field = "poly"
        fields = ("provider", "price", "name", "poly")

    def to_representation(self, instance):
        result = super().to_representation(instance)
        if self.context["action"] == "list":
            return result["properties"]
        return result
