from django.contrib import admin

from .models import Company, Branch, Department


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active', 'country', 'phone', 'planWrapper', 'created_at', 'updated_at')
    search_fields = ('title', 'phone')
    list_filter = ('is_active', 'country')
    date_hierarchy = 'created_at'


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'address', 'lat', 'lng', 'radius', 'city', 'company', 'createdAt', 'updatedAt')
    search_fields = ('title', 'address')
    list_filter = ('city', 'company')
    date_hierarchy = 'createdAt'


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'branch', 'company', 'createdAt', 'updatedAt')
    search_fields = ('title',)
    list_filter = ('branch', 'company')
    date_hierarchy = 'createdAt'