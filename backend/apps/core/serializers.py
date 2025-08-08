from rest_framework import serializers
from .models import (
    Historical,
    Base,
)

class HistoricalWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historical
        exclude = ("polymorphic_ctype",)

class HistoricalReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Historical
        exclude = ("polymorphic_ctype",)


class BaseWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        exclude = ("polymorphic_ctype",)

class BaseReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Base
        exclude = ("polymorphic_ctype",)

