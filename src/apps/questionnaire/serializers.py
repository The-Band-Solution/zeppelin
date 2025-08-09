from rest_framework import serializers
from .models import (
    AdoptedLevel,
    Statement,
    FeedbackQuestionnaire,
    Questionnaire,
    QuestionnaireExcel,
    Answer,
)

class AdoptedLevelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptedLevel
       

class AdoptedLevelReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = AdoptedLevel
       


class StatementWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
       

class StatementReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Statement
       


class FeedbackQuestionnaireWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackQuestionnaire
       

class FeedbackQuestionnaireReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = FeedbackQuestionnaire
       


class QuestionnaireWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
       

class QuestionnaireReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Questionnaire
       


class QuestionnaireExcelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireExcel
       

class QuestionnaireExcelReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = QuestionnaireExcel
       


class AnswerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
       

class AnswerReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Answer
       

