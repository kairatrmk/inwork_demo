from django.db import models


class Country(models.Model):
    title = models.CharField(max_length=128)
    phone_code = models.CharField(max_length=128)
    phone_pattern = models.CharField(max_length=128)
    icon = models.ImageField(upload_to='country_icon')
    createAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=128)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


