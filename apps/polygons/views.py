from typing import Any, Dict

from django.contrib.gis.geos import Point
from django.db.models import QuerySet
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Polygon
from .serializers import PolygonCreateSerializer


class PolygonViewSet(ModelViewSet):

    queryset = Polygon.objects.all()
    serializer_class = PolygonCreateSerializer

    def get_queryset(self) -> QuerySet[Polygon]:
        params = self.request.query_params
        if params.get("lat") and params.get("lng"):
            return (
                super()
                .get_queryset()
                .filter(
                    poly__contains=Point(
                        float(params.get("lng")), float(params.get("lat"))
                    )
                )
            )
        return super().get_queryset()

    def get_serializer_context(self) -> Dict[str, Any]:
        context = super().get_serializer_context()
        context["action"] = self.action
        return context

    @extend_schema(
        request=PolygonCreateSerializer,
        responses={200: PolygonCreateSerializer(many=True), 400: None},
        parameters=[
            OpenApiParameter(
                name="lat",
                description="Latitude Coordinate",
                required=False,
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name="lng",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Longitude Coordinate",
                required=False,
            ),
        ],
    )
    @method_decorator(cache_page(60 * 60))
    @method_decorator(vary_on_cookie)
    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return super().list(request, *args, **kwargs)
