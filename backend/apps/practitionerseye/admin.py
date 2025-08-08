from django.contrib import admin
from .models import Dimension,Element

@admin.register(Dimension)
class DimensionAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

