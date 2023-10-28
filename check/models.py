from django.db import models

from companies.models import Company, Branch
from employee.models import Employee
from schedules.models import EmployeeSchedule
from countries.models import City


class Check(models.Model):
    date = models.DateField()
    check_in = models.TimeField()
    date_in = models.DateField()
    lat_in = models.DecimalField(max_digits=9, decimal_places=6)
    lng_in = models.DecimalField(max_digits=9, decimal_places=6)
    check_out = models.TimeField()
    date_out = models.DateField()
    lat_out = models.DecimalField(max_digits=9, decimal_places=6)
    lng_out = models.DecimalField(max_digits=9, decimal_places=6)
    schedule_start = models.DateField()
    schedule_end = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    schedule = models.ForeignKey(EmployeeSchedule, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    grace_in = models.TimeField(help_text='Начало перерыва')
    grace_out = models.TimeField(help_text='Конец перерыва')
