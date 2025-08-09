from rest_framework import serializers
from .models import (
    OrganizationCategory,
    Size,
    OrganizationType,
    Region,
    State,
    Organization,
)

class OrganizationCategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationCategory
       

class OrganizationCategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = OrganizationCategory
       


class SizeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
       

class SizeReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Size
       


class OrganizationTypeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationType
       

class OrganizationTypeReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = OrganizationType
       


class RegionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
       

class RegionReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Region
       


class StateWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
       

class StateReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = State
       


class OrganizationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
       

class OrganizationReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Organization
       

