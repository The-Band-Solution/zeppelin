from rest_framework import serializers
from .models import (
    Dimension,
    Element,
)

class DimensionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dimension
        exclude = ("polymorphic_ctype",)

class DimensionReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Dimension
        exclude = ("polymorphic_ctype",)


class ElementWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        exclude = ("polymorphic_ctype",)

class ElementReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Element
        exclude = ("polymorphic_ctype",)

