from django.contrib import admin
from .models import Employee, Position
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender', 'employee_company', 'employee_branch', 'employee_department', 'employee_position', 'createdAt', 'updatedAt')

    search_fields = ()
    list_filter = ('id', )


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'position_branch', 'position_department', 'position_company', 'createdAt', 'updatedAt')
    search_fields = ('title',)
    date_hierarchy = 'createdAt'