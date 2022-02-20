from typing import Any

from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Provider
from .serializers import ProviderSerializer

# Create your views here.


class ProviderLCAPIView(ListCreateAPIView):

    queryset = Provider.objects.filter(is_active=True)
    serializer_class = ProviderSerializer

    def get_queryset(self) -> QuerySet[Provider]:
        return super().get_queryset()

    @extend_schema(
        request=ProviderSerializer,
        responses={201: ProviderSerializer, 400: None},
    )
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return super().create(request, *args, **kwargs)

    @extend_schema(
        request=ProviderSerializer,
        responses={200: ProviderSerializer(many=True), 400: None},
    )
    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return super().list(request, *args, **kwargs)


class ProviderRUDAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Provider.objects.filter(is_active=True)
    serializer_class = ProviderSerializer
