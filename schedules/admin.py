from django.contrib import admin

from .models import EmployeeSchedule, WorkingDay, ScheduleType, LeaveType
from .parametrs import ScheduleParameters


@admin.register(EmployeeSchedule)
class EmployeeScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'leave_type', 'timezone', 'time_start', 'time_end', 'break_time', 'grace_start',
                    'grace_end', 'boundary_start', 'boundary_end', 'time_planned', 'location_id', 'department_id', 'position_id',
                    'employees_id', 'period_from', 'period_to', 'is_active', 'working_days', 'custom_time', 'schedule_repeat_type',
                    'schedule_parameters')
    search_fields = ('schedule_type',)


@admin.register(WorkingDay)
class WorkingDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'time_start', 'time_end')
    list_filter = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')


@admin.register(ScheduleParameters)
class ScheduleParametersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'work_days', 'off_days')
    search_fields = ('title',)


@admin.register(ScheduleType)
class ScheduleTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title',)


@admin.register(LeaveType)
class LeaveTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title',)
