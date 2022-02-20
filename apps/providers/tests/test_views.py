import json

import factory
import pytest
from django.urls import reverse
from rest_framework import status

from apps.providers import views
from apps.providers.tests.factories import ProviderFactory

pytestmark = pytest.mark.django_db


class TestProviderEndpoints:
    def test_provider_list(self, rf):

        url = reverse("providers:provider-lc")
        no_of_objs = 5
        request = rf.get(url)
        view = views.ProviderLCAPIView.as_view()
        ProviderFactory.create_batch(no_of_objs, is_active=True)
        response = view(request).render()
        assert len(json.loads(response.content)) == no_of_objs

    def test_provider_create(self, rf):

        url = reverse("providers:provider-lc")
        obj = factory.build(dict, FACTORY_CLASS=ProviderFactory, language="en")
        request = rf.post(url, content_type="application/json", data=json.dumps(obj))
        view = views.ProviderLCAPIView.as_view()
        response = view(request).render()
        assert "id" in json.loads(response.content)

    def test_provider_read(self, rf):

        provider = ProviderFactory(is_active=True)
        url = reverse("providers:provider-rud", args=[provider.id])
        request = rf.get(url)
        view = views.ProviderRUDAPIView.as_view()
        response = view(request, pk=provider.id).render()
        assert json.loads(response.content)["id"] == provider.id

    @pytest.mark.parametrize(
        "field", ["name", "phone_number", "language", "currency", "email"]
    )
    def test_provider_patch(self, rf, field):

        old_provider = ProviderFactory(is_active=True)
        provider = factory.build(dict, FACTORY_CLASS=ProviderFactory)
        valid_field = {field: provider[field]}
        url = reverse("providers:provider-rud", args=[old_provider.id])
        request = rf.patch(
            url, content_type="application/json", data=json.dumps(valid_field)
        )
        view = views.ProviderRUDAPIView.as_view()
        response = view(request, pk=old_provider.id).render()
        assert json.loads(response.content)[field] == valid_field[field]
        assert json.loads(response.content)["id"] == old_provider.id

    def test_provider_put(self, rf):

        old_provider = ProviderFactory(is_active=True)
        provider = factory.build(dict, FACTORY_CLASS=ProviderFactory)
        url = reverse("providers:provider-rud", args=[old_provider.id])
        request = rf.put(
            url, content_type="application/json", data=json.dumps(provider)
        )
        view = views.ProviderRUDAPIView.as_view()
        response = view(request, pk=old_provider.id).render()
        assert json.loads(response.content)["id"] == old_provider.id
        assert json.loads(response.content)["name"] != old_provider.name

    def test_provider_delete(self, rf):

        old_provider = ProviderFactory(is_active=True)
        url = reverse("providers:provider-rud", args=[old_provider.id])
        request = rf.delete(url)
        view = views.ProviderRUDAPIView.as_view()
        response = view(request, pk=old_provider.id).render()
        assert response.status_code == status.HTTP_204_NO_CONTENT
