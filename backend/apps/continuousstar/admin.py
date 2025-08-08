from django.contrib import admin
from .models import ContinuousPhase,ContinuousActivity

@admin.register(ContinuousPhase)
class ContinuousPhaseAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

@admin.register(ContinuousActivity)
class ContinuousActivityAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

