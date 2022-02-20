from django.urls import path

from .views import ProviderLCAPIView, ProviderRUDAPIView

app_name = "providers"
urlpatterns = [
    path("", ProviderLCAPIView.as_view(), name="provider-lc"),
    path("<int:pk>/", ProviderRUDAPIView.as_view(), name="provider-rud"),
]
