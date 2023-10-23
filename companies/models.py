from django.db import models

from countries.models import City, Country
from schedules.parametrs import ScheduleParameters


class Company(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    logo = models.ImageField(upload_to='company_logo')
    is_active = models.BooleanField(default=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16)
    planWrapper = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Branch(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=256,null=True,blank=True)
    address = models.CharField(max_length=128)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    radius = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Department(models.Model):
    title = models.CharField(max_length=128)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
