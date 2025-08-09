from rest_framework import serializers
from .models import (
    Process,
)

class ProcessWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
       

class ProcessReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Process
       

