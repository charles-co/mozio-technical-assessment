from rest_framework.routers import DefaultRouter

from .views import PolygonViewSet

router = DefaultRouter()
router.register(r"", PolygonViewSet)

app_name = "polygons"
urlpatterns = [] + router.urls
