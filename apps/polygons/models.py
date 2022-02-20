from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

from apps.providers.models import Provider


class Polygon(models.Model):

    provider = models.ForeignKey(
        Provider,
        verbose_name=_("Provider"),
        on_delete=models.CASCADE,
        related_name="polygons",
    )
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    poly = models.PolygonField(_("Polygon"), srid=4326)

    def __str__(self) -> str:
        return f"Polygon: {self.provider.name}"
