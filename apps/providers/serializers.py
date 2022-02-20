from phonenumber_field import serializerfields
from rest_framework import serializers

from .constants import iso_639_choices
from .models import Provider


class ProviderSerializer(serializers.ModelSerializer):

    language = serializers.ChoiceField(choices=iso_639_choices, required=True)
    currency = serializers.CharField(required=True, max_length=3)
    phone_number = serializerfields.PhoneNumberField()

    class Meta:
        model = Provider
        exclude = ("is_active",)
