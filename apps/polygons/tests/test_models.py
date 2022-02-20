import pytest
from django.db import IntegrityError

from apps.polygons.models import Polygon
from apps.polygons.tests.factories import PolygonFactory

pytestmark = pytest.mark.django_db


class TestPolygonModels:
    def test_polygon_create(self):
        PolygonFactory()
        PolygonFactory()
        assert Polygon.objects.all().count() == 2

    def test_polygon_create_with_same_provider(self):
        polygon = PolygonFactory()
        with pytest.raises(IntegrityError):
            PolygonFactory(poly=polygon.poly, provider=polygon.provider)
            raise IntegrityError("unique_provider_polygon")
