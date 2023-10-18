from django.contrib import admin

from .models import User, EmployeeSchedule, Employee, WorkingDay


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')


@admin.register(EmployeeSchedule)
class EmployeeScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'schedule_type', 'period_from', 'period_to', 'timezone')
    search_fields = ('schedule_type',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'position', 'department', 'branch')
    search_fields = ('user__username', 'position', 'department', 'branch')
    list_filter = ('department', 'branch')


@admin.register(WorkingDay)
class WorkingDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    list_filter = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
