from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from iso639 import Lang
from iso639.exceptions import InvalidLanguageValue
from iso4217 import Currency


def validate_lang(value):
    try:
        Lang(value)
    except InvalidLanguageValue:
        ValidationError(
            _("%(value)s is not a valid language code"),
            params={"value": value},
        )
    return value


def validate_currency(value):
    try:
        Currency(value.upper())
    except ValueError:
        ValidationError(
            _("%(value)s is not a valid currency code"),
            params={"value": value},
        )
    return value
