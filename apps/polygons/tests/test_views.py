import json

import factory
import pytest
from django.urls import reverse
from rest_framework import status

from apps.polygons.tests.factories import PolygonFactory
from apps.polygons.views import PolygonViewSet
from apps.providers.tests.factories import ProviderFactory

pytestmark = pytest.mark.django_db


class TestPolygonEndpoints:

    url = "/polygons/"

    def test_polygon_list(self, rf):

        url = reverse("polygons:polygon-list")
        no_of_objs = 5
        request = rf.get(url)
        view = PolygonViewSet.as_view({"get": "list"})
        PolygonFactory.create_batch(no_of_objs)
        response = view(request).render()
        assert len(json.loads(response.content)["features"]) == no_of_objs

    def test_polygon_create(self, rf):

        obj = factory.build(dict, FACTORY_CLASS=PolygonFactory)
        provider = ProviderFactory()
        obj["provider"] = provider.id
        obj["poly"] = str(obj["poly"])
        request = rf.post(
            self.url, content_type="application/json", data=json.dumps(obj)
        )
        view = PolygonViewSet.as_view({"post": "create"})
        response = view(request).render()
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.parametrize("field", ["price", "poly"])
    def test_polygon_patch(self, rf, field):

        old_polygon = PolygonFactory()
        polygon = factory.build(dict, FACTORY_CLASS=PolygonFactory)
        if field == "poly":
            valid_field = {field: str(polygon[field])}
        else:
            valid_field = {field: polygon[field]}
        request = rf.patch(
            self.url + f"{old_polygon.id}/",
            content_type="application/json",
            data=json.dumps(valid_field),
        )
        view = PolygonViewSet.as_view({"patch": "partial_update"})
        response = view(request, pk=old_polygon.id).render()
        if field not in ["poly", "id"]:
            assert float(json.loads(response.content)["properties"][field]) == float(
                valid_field[field]
            )
        elif field == "poly":
            assert (
                json.loads(response.content)["geometry"]["coordinates"]
                != old_polygon.poly.coords
            )
        assert json.loads(response.content)["id"] == old_polygon.id
