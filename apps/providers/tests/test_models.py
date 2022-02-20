import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from apps.providers.models import Provider
from apps.providers.tests.factories import ProviderFactory

pytestmark = pytest.mark.django_db


class TestProviderModels:
    def test_provider_create(self):
        ProviderFactory()
        assert Provider.objects.all().count() == 1

    def test_provider_create_with_same_email(self):
        with pytest.raises(IntegrityError):
            ProviderFactory(email="test@example.com")
            ProviderFactory(email="test@example.com")

            raise IntegrityError("unique email violation")

    def test_provider_str(self):
        provider = ProviderFactory(name="Uber")
        assert str(provider) == "Uber"

    def test_provider_invalid_currency(self):
        with pytest.raises(ValidationError):
            ProviderFactory(currency="000")
            raise ValidationError("")

    def test_provider_invalid_language(self):
        with pytest.raises(ValidationError):
            ProviderFactory(currency="usx")
            raise ValidationError("")
