from django.contrib import admin
from .models import AdoptedLevel,Statement,FeedbackQuestionnaire,Questionnaire,QuestionnaireExcel,Answer

@admin.register(AdoptedLevel)
class AdoptedLevelAdmin(admin.ModelAdmin):
    list_display = ['id', 'percentage']
    list_display_links = ['id', 'percentage']
    search_fields = ['id', 'percentage']
    list_per_page = 25
    ordering = ['-id']

@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'statement']
    list_display_links = ['id', 'code', 'statement']
    search_fields = ['id', 'code', 'statement']
    list_per_page = 25
    ordering = ['-id']

@admin.register(FeedbackQuestionnaire)
class FeedbackQuestionnaireAdmin(admin.ModelAdmin):
    list_display = ['id', 'collected_date']
    list_display_links = ['id', 'collected_date']
    search_fields = ['id', 'collected_date']
    list_per_page = 25
    ordering = ['-id']

@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ['id', 'applied_date']
    list_display_links = ['id', 'applied_date']
    search_fields = ['id', 'applied_date']
    list_per_page = 25
    ordering = ['-id']

@admin.register(QuestionnaireExcel)
class QuestionnaireExcelAdmin(admin.ModelAdmin):
    list_display = ['id',]
    list_display_links = ['id',]
    search_fields = ['id',]
    list_per_page = 25
    ordering = ['-id']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment']
    list_display_links = ['id', 'comment']
    search_fields = ['id', 'comment']
    list_per_page = 25
    ordering = ['-id']

