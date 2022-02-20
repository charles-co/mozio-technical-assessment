from factory import Faker, lazy_attribute
from factory.django import DjangoModelFactory

from apps.providers.models import Provider


class ProviderFactory(DjangoModelFactory):

    name = Faker("company")
    email = Faker("ascii_free_email")
    phone_number = "+2347084839200"
    currency = "USD"
    is_active = Faker("pybool")

    class Meta:
        model = Provider
        django_get_or_create = ["email"]

    @lazy_attribute
    def language(self):
        language = Faker._get_faker().country_code().lower()
        return language
