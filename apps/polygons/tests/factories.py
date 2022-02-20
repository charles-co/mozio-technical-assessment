import random

import faker
from django.contrib.gis.geos import LinearRing, Polygon
from factory import Faker, SubFactory, fuzzy
from factory.django import DjangoModelFactory

from apps.polygons.models import Polygon as _Polygon
from apps.providers.tests.factories import ProviderFactory

_Faker = faker.Faker()


class FuzzyPolygon(fuzzy.BaseFuzzyAttribute):
    """Yields random polygon"""

    def __init__(self, length=None, **kwargs):
        if length is None:
            length = random.randrange(3, 20, 1)
        if length < 3:
            raise Exception("Polygon needs to be 3 or greater in length.")
        self.length = length
        super().__init__(**kwargs)

    def get_random_coords(self):
        coord = list(_Faker.local_latlng(coords_only=True))
        return [float(x) for x in coord]

    def fuzz(self):
        prefix = suffix = self.get_random_coords()
        coords = [self.get_random_coords() for __ in range(self.length - 1)]
        all_coords = [prefix] + coords + [suffix]
        return Polygon(((LinearRing(all_coords))))


class PolygonFactory(DjangoModelFactory):

    provider = SubFactory(ProviderFactory)
    price = Faker(
        "pyfloat", right_digits=2, left_digits=7, positive=True, min_value=100.00
    )
    poly = FuzzyPolygon()

    class Meta:
        model = _Polygon
