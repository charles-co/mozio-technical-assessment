from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Polygon


class BasePolygonSerializer(GeoFeatureModelSerializer):

    name = serializers.CharField(source="provider.name", read_only=True)

    class Meta:
        model = Polygon
        geo_field = "poly"
        fields = ("id", "price", "name", "poly", "provider")

    def validate(self, attrs):
        if Polygon.objects.filter(
            poly=attrs.get("poly"), provider=attrs.get("provider")
        ).exists():
            raise serializers.ValidationError("Polygon already exists for provider")
        return super().validate(attrs)

    def to_representation(self, instance):
        result = super().to_representation(instance)
        if self.context["action"] == "list":
            return result["properties"]
        return result


class PolygonSerializer(BasePolygonSerializer):
    class Meta(BasePolygonSerializer.Meta):
        read_only_fields = ["provider"]
