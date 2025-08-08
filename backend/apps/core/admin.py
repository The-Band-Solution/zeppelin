from django.contrib import admin
from .models import Historical,Base

@admin.register(Historical)
class HistoricalAdmin(admin.ModelAdmin):
4list_display = ['id', 'create_at', 'modified_at']
4list_display_links = ['id', 'create_at', 'modified_at']
4search_fields = ['id', 'create_at', 'modified_at']
4list_per_page = 25
4ordering = ['-id']

@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
4list_display = ['id', 'nome', 'descricao']
4list_display_links = ['id', 'nome', 'descricao']
4search_fields = ['id', 'nome', 'descricao']
4list_per_page = 25
4ordering = ['-id']

