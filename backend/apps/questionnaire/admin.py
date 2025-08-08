from django.contrib import admin
from .models import AdoptedLevel,Statement,FeedbackQuestionnaire,Questionnaire,QuestionnaireExcel,Answer

@admin.register(AdoptedLevel)
class AdoptedLevelAdmin(admin.ModelAdmin):
4list_display = ['id', 'percentage']
4list_display_links = ['id', 'percentage']
4search_fields = ['id', 'percentage']
4list_per_page = 25
4ordering = ['-id']

@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
4list_display = ['id', 'code', 'statement']
4list_display_links = ['id', 'code', 'statement']
4search_fields = ['id', 'code', 'statement']
4list_per_page = 25
4ordering = ['-id']

@admin.register(FeedbackQuestionnaire)
class FeedbackQuestionnaireAdmin(admin.ModelAdmin):
4list_display = ['id', 'collected_date']
4list_display_links = ['id', 'collected_date']
4search_fields = ['id', 'collected_date']
4list_per_page = 25
4ordering = ['-id']

@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
4list_display = ['id', 'applied_date']
4list_display_links = ['id', 'applied_date']
4search_fields = ['id', 'applied_date']
4list_per_page = 25
4ordering = ['-id']

@admin.register(QuestionnaireExcel)
class QuestionnaireExcelAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
4list_display = ['id', 'comment']
4list_display_links = ['id', 'comment']
4search_fields = ['id', 'comment']
4list_per_page = 25
4ordering = ['-id']

