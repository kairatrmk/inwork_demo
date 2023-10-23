import os
import django
from datetime import date
import datetime


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  # Replace with your actual project name

# Call setup() to configure Django settings
django.setup()

from schedules.models import Employee,  ScheduleParameters

#
# Replace 'employee_id' with the actual ID of the employee you want to check
# employee_id = 1  # Replace with the actual employee ID
# employee = Employee.objects.get(id=employee_id)  # Get the Employee instance
#
# # Access the related EmployeeSchedule
# employee_schedule = employee.employee_schedule
#
# # Check if the employee works on Sundays
# works_on_sunday = employee_schedule.working_days.sunday
#
# # Now you can use the `works_on_sunday` variable to determine if the employee works on Sundays or not
# if works_on_sunday:
#     print("The employee works on Sundays.")
# else:
#     print("The employee has a day off on Sundays.")




# from schedules.models import Employee
#
# employee_id = 1  # Replace with the actual employee ID
# target_date = date(2023, 10, 20)  # Replace with the target date
#
# employee = Employee.objects.get(id=2)  # Get the Employee instance
#
# # Access the related EmployeeSchedule
# employee_schedule = employee.employee_schedule
#
# # Check if the employee works on the target date (e.g., '2023-10-20')
# target_day = target_date.strftime('%A').lower()
# works_on_target_date = getattr(employee_schedule.working_days, target_day)
#
# # Now you can use the `works_on_target_date` variable to determine if the employee works on the target date or has a day off.
# if works_on_target_date:
#     # Получите время начала и окончания рабочего дня
#     start_time = employee_schedule.worktime_start
#     end_time = employee_schedule.worktime_end
#
#     print(f"The employee works on {target_date}.")
#     print(f"Work hours: {start_time} to {end_time}")
# else:
#     print(f"The employee has a day off on {target_date}.")


from datetime import date, timedelta

# выводит весь его рабочий график
def is_workday_in_variable_schedule(start_date, target_date, work_days, off_days):
    current_date = start_date
    is_workday = True
    results = []

    while current_date <= target_date:
        for _ in range(work_days):
            results.append(True)
            current_date += timedelta(days=1)

        for _ in range(off_days):
            results.append(False)
            current_date += timedelta(days=1)

    return results

# Пример использования
start_date = date(2023, 10, 1)  # Начало графика
target_date = date(2023, 11, 12)  # Целевая дата
work_days = 1
off_days = 3

results = is_workday_in_variable_schedule(start_date, target_date, work_days, off_days)

for day, result in enumerate(results, start=1):
    if result:
        print(f"Day {day}: True (The employee works)")
    else:
        print(f"Day {day}: False (The employee has a day off)")