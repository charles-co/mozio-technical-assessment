from phonenumber_field import serializerfields
from rest_framework import serializers

from .models import Provider


class ProviderSerializer(serializers.ModelSerializer):

    language = serializers.CharField(max_length=3, required=True)
    currency = serializers.CharField(required=True, max_length=3)
    phone_number = serializerfields.PhoneNumberField()

    class Meta:
        model = Provider
        exclude = ("is_active",)
