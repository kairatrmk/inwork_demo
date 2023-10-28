from django.db import models
from timezone_field import TimeZoneField
from datetime import time, timedelta

from companies.models import Branch, Department
from employee.models import Position, Employee
from .parametrs import ScheduleParameters


class WorkingDay(models.Model):
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=True)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=True)
    friday = models.BooleanField(default=True)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)
    time_start = models.TimeField(default=time(9, 0))
    time_end = models.TimeField(default=time(18, 0))


class ScheduleType(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class LeaveType(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


# https://pypi.org/project/django-timezone-field/
class EmployeeSchedule(models.Model):
    title = models.CharField(max_length=255)
    type = models.ForeignKey(ScheduleType, on_delete=models.CASCADE, help_text='Тип расписания')
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE, help_text='Тип пропуска', null=True)
    timezone = TimeZoneField(default='UTC')
    time_start = models.TimeField(default=time(9, 0))
    time_end = models.TimeField(default=time(18, 0))
    break_time = models.PositiveIntegerField(default=1, help_text='Количество часов перерыва')
    grace_start = models.TimeField(default=time(12, 0))
    grace_end = models.TimeField(default=time(13, 0))
    boundary_start = models.TimeField(default=time(9, 0), help_text='Вверхняя граница расписания')
    boundary_end = models.TimeField(default=time(18, 0), help_text='Нижняя граница расписания')
    time_planned = models.PositiveIntegerField(default=8, help_text='Количество рабочих часов для свободного графика')
    location_id = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    period_from = models.DateField()
    period_to = models.DateField()
    employees_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    working_days = models.ForeignKey(WorkingDay, on_delete=models.CASCADE, null=True, blank=True)
    custom_time = models.JSONField(null=True, blank=True, default=None, help_text='Выбор индивидуального времени работы для рабочих дней ')
    schedule_repeat_type = models.CharField(max_length=255, help_text='Тип повтора расписания', choices=(('individual', 'Разное время для каждого дня'), ('common', 'Единое время для выбранных дней')))
    schedule_parameters = models.ForeignKey(ScheduleParameters, on_delete=models.CASCADE, null=True, blank=True)

    # todo: add break time logic

    def get_starting_day(self):
        current_day = self.period_from
        while not getattr(self.working_days, current_day.strftime('%A').lower()):
            current_day += timedelta(days=1)
        return current_day


