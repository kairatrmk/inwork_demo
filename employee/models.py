from django.db import models

from companies.models import Company, Branch, Department


class Position(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    position_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    position_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Employee(models.Model):
    gender = models.CharField(max_length=128)
    employee_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    employee_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee_position = models.ForeignKey(Position, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

