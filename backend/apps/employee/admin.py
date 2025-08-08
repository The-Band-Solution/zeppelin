from django.contrib import admin
from .models import AcademicDegreeCategory,AcademicDegree,AcademicDegreeStatus,KnwoledgeLevel,ExperienceLevel,Position,Employee,EmployeeKnowledge,SthStageKnwoledgeLevel,SthStageExperienceLevel,Team

@admin.register(AcademicDegreeCategory)
class AcademicDegreeCategoryAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

@admin.register(AcademicDegree)
class AcademicDegreeAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

@admin.register(AcademicDegreeStatus)
class AcademicDegreeStatusAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

@admin.register(KnwoledgeLevel)
class KnwoledgeLevelAdmin(admin.ModelAdmin):
4list_display = ['id', 'value']
4list_display_links = ['id', 'value']
4search_fields = ['id', 'value']
4list_per_page = 25
4ordering = ['-id']

@admin.register(ExperienceLevel)
class ExperienceLevelAdmin(admin.ModelAdmin):
4list_display = ['id', 'value']
4list_display_links = ['id', 'value']
4search_fields = ['id', 'value']
4list_per_page = 25
4ordering = ['-id']

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
4list_display = ['id', 'e_mail', 'role']
4list_display_links = ['id', 'e_mail', 'role']
4search_fields = ['id', 'e_mail', 'role']
4list_per_page = 25
4ordering = ['-id']

@admin.register(EmployeeKnowledge)
class EmployeeKnowledgeAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

@admin.register(SthStageKnwoledgeLevel)
class SthStageKnwoledgeLevelAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

@admin.register(SthStageExperienceLevel)
class SthStageExperienceLevelAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

