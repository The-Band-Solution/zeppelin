from django.urls import path, register_converter, include
from rest_framework import routers
from .api_views import (
    RegistrarUsuarioViewSet,
)

router = routers.DefaultRouter()
router.register(r'register', RegistrarUsuarioViewSet, basename='register')

urlpatterns = [
    path('auth/', include(router.urls))
]