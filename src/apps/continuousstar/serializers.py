from rest_framework import serializers
from .models import (
    ContinuousPhase,
    ContinuousActivity,
)

class ContinuousPhaseWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContinuousPhase
       

class ContinuousPhaseReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = ContinuousPhase
       


class ContinuousActivityWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContinuousActivity
       

class ContinuousActivityReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = ContinuousActivity
       

