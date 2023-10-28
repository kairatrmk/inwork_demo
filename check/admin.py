from django.contrib import admin

# Register your models here
from .models import Check


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ('date', 'check_in', 'date_in', 'check_out', 'date_out', 'employee', 'company', 'branch', 'city', 'createdAt', 'updatedAt')

    # Остальные параметры админки, если нужны
    search_fields = ('employee__user__first_name', 'employee__user__last_name', 'company__name', 'branch__name', 'city__name')
    list_filter = ('company', 'branch', 'city')
    date_hierarchy = 'date'