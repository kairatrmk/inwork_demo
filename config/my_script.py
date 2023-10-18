import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  # Replace with your actual project name

# Call setup() to configure Django settings
django.setup()

# from schedules.models import Employee
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

from datetime import date
from schedules.models import Employee


employee_id = 1  # Replace with the actual employee ID
target_date = date(2023, 10, 20)  # Replace with the target date

employee = Employee.objects.get(id=2)  # Get the Employee instance

# Access the related EmployeeSchedule
employee_schedule = employee.employee_schedule

# Check if the employee works on the target date (e.g., '2023-10-20')
target_day = target_date.strftime('%A').lower()
works_on_target_date = getattr(employee_schedule.working_days, target_day)

# Now you can use the `works_on_target_date` variable to determine if the employee works on the target date or has a day off.
if works_on_target_date:
    print(f"The employee works on {target_date}.")
else:
    print(f"The employee has a day off on {target_date}.")
