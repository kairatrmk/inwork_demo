# Generated by Django 4.2.6 on 2023-10-27 09:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '__first__'),
        ('employee', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleParameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('work_days', models.PositiveIntegerField()),
                ('off_days', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.BooleanField(default=True)),
                ('tuesday', models.BooleanField(default=True)),
                ('wednesday', models.BooleanField(default=True)),
                ('thursday', models.BooleanField(default=True)),
                ('friday', models.BooleanField(default=True)),
                ('saturday', models.BooleanField(default=False)),
                ('sunday', models.BooleanField(default=False)),
                ('time_start', models.TimeField(default=datetime.time(9, 0))),
                ('time_end', models.TimeField(default=datetime.time(18, 0))),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('timezone', timezone_field.fields.TimeZoneField(default='UTC')),
                ('time_start', models.TimeField(default=datetime.time(9, 0))),
                ('time_end', models.TimeField(default=datetime.time(18, 0))),
                ('break_time', models.PositiveIntegerField(default=1, help_text='Количество часов перерыва')),
                ('grace_start', models.TimeField(default=datetime.time(12, 0))),
                ('grace_end', models.TimeField(default=datetime.time(13, 0))),
                ('boundary_start', models.TimeField(default=datetime.time(9, 0), help_text='Вверхняя граница расписания')),
                ('boundary_end', models.TimeField(default=datetime.time(18, 0), help_text='Нижняя граница расписания')),
                ('time_planned', models.PositiveIntegerField(default=8, help_text='Количество рабочих часов для свободного графика')),
                ('period_from', models.DateField()),
                ('period_to', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('custom_time', models.JSONField(blank=True, default=None, help_text='Выбор индивидуального времени работы для рабочих дней ', null=True)),
                ('schedule_repeat_type', models.CharField(choices=[('individual', 'Разное время для каждого дня'), ('common', 'Единое время для выбранных дней')], help_text='Тип повтора расписания', max_length=255)),
                ('department_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.department')),
                ('employees_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('leave_type', models.ForeignKey(help_text='Тип пропуска', null=True, on_delete=django.db.models.deletion.CASCADE, to='schedules.leavetype')),
                ('location_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.branch')),
                ('position_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.position')),
                ('schedule_parameters', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedules.scheduleparameters')),
                ('type', models.ForeignKey(help_text='Тип расписания', on_delete=django.db.models.deletion.CASCADE, to='schedules.scheduletype')),
                ('working_days', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedules.workingday')),
            ],
        ),
    ]
