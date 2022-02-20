from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .validators import validate_currency, validate_lang

# Create your models here.


class Provider(models.Model):

    name = models.CharField(_("Name"), max_length=255)
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    phone_number = PhoneNumberField(_("Phone Number"))
    language = models.CharField(
        _("Language"), validators=[validate_lang], default="en", max_length=3
    )
    currency = models.CharField(
        _("Currency"), validators=[validate_currency], default="USD", max_length=3
    )
    is_active = models.BooleanField(_("Is Active?"), default=True)

    class Meta:
        ordering = ["name", "email"]
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    def __str__(self) -> str:
        return self.name
