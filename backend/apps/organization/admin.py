from django.contrib import admin
from .models import OrganizationCategory,Size,OrganizationType,Region,State,Organization

@admin.register(OrganizationCategory)
class OrganizationCategoryAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

@admin.register(OrganizationType)
class OrganizationTypeAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
4list_display = ['id',]
4list_display_links = ['id',]
4search_fields = ['id',]
4list_per_page = 25
4ordering = ['-id']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
4list_display = ['id', 'latitude', 'longitude']
4list_display_links = ['id', 'latitude', 'longitude']
4search_fields = ['id', 'latitude', 'longitude']
4list_per_page = 25
4ordering = ['-id']

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
4list_display = ['id', 'age']
4list_display_links = ['id', 'age']
4search_fields = ['id', 'age']
4list_per_page = 25
4ordering = ['-id']

