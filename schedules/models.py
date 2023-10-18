from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models
from timezone_field import TimeZoneField
from datetime import time, timedelta


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class WorkingDay(models.Model):
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=True)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=True)
    friday = models.BooleanField(default=True)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)


# https://pypi.org/project/django-timezone-field/
class EmployeeSchedule(models.Model):
    schedule_type = models.CharField(max_length=255, help_text='Тип расписаний')
    period_from = models.DateField()
    period_to = models.DateField()
    worktime_start = models.TimeField(default=time(9, 0))
    worktime_end = models.TimeField(default=time(18, 0))
    timezone = TimeZoneField(default='UTC')
    schedule_repeat_type = models.CharField(max_length=255, help_text='Тип повтора расписания')
    working_days = models.ForeignKey(WorkingDay, on_delete=models.CASCADE)
    # todo: add break time logic

    def get_starting_day(self):
        current_day = self.period_from
        while not getattr(self.working_days, current_day.strftime('%A').lower()):
            current_day += timedelta(days=1)
        return current_day


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=128)
    department = models.CharField(max_length=128)
    branch = models.CharField(max_length=128)
    employee_schedule = models.ForeignKey(EmployeeSchedule, on_delete=models.CASCADE)


class Position(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    branch = models.CharField(max_length=128)
    department = models.CharField(max_length=128)
    working_days = models.ForeignKey(WorkingDay, on_delete=models.CASCADE)
    employee_schedule = models.ForeignKey(EmployeeSchedule, on_delete=models.CASCADE)




