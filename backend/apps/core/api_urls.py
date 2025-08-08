from django.urls import path, register_converter, include
from rest_framework import routers
from .api_views import (
    HistoricalViewSet,
    BaseViewSet,
)
router = routers.DefaultRouter()

router.register(r'historical', HistoricalViewSet, basename='historical')
router.register(r'base', BaseViewSet, basename='base')

urlpatterns = [
    path('core/', include(router.urls))
]
