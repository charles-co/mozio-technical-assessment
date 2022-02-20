from rest_framework.routers import DefaultRouter

from .views import PolygonViewSet

router = DefaultRouter()
router.register(r"", PolygonViewSet, basename="polygon")

app_name = "polygons"
urlpatterns = [] + router.urls
