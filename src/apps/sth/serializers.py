from rest_framework import serializers
from .models import (
    Stage,
)

class StageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
       

class StageReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Stage
       

