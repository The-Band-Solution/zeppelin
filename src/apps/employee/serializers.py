from rest_framework import serializers
from .models import (
    AcademicDegreeCategory,
    AcademicDegree,
    AcademicDegreeStatus,
    KnwoledgeLevel,
    ExperienceLevel,
    Position,
    Employee,
    EmployeeKnowledge,
    SthStageKnwoledgeLevel,
    SthStageExperienceLevel,
    Team,
)

class AcademicDegreeCategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicDegreeCategory
       

class AcademicDegreeCategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = AcademicDegreeCategory
       


class AcademicDegreeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicDegree
       

class AcademicDegreeReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = AcademicDegree
       


class AcademicDegreeStatusWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicDegreeStatus
       

class AcademicDegreeStatusReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = AcademicDegreeStatus
       


class KnwoledgeLevelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnwoledgeLevel
       

class KnwoledgeLevelReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = KnwoledgeLevel
       


class ExperienceLevelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceLevel
       

class ExperienceLevelReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = ExperienceLevel
       


class PositionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
       

class PositionReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Position
       


class EmployeeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
       

class EmployeeReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Employee
       


class EmployeeKnowledgeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeKnowledge
       

class EmployeeKnowledgeReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = EmployeeKnowledge
       


class SthStageKnwoledgeLevelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SthStageKnwoledgeLevel
       

class SthStageKnwoledgeLevelReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = SthStageKnwoledgeLevel
       


class SthStageExperienceLevelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SthStageExperienceLevel
       

class SthStageExperienceLevelReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = SthStageExperienceLevel
       


class TeamWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
       

class TeamReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Team
       

