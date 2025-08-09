from rest_framework import serializers
from .models import (
    Dimension,
    Element,
)

class DimensionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dimension
       

class DimensionReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Dimension
       


class ElementWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
       

class ElementReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Element
       

