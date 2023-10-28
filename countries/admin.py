from django.contrib import admin

from .models import Country, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone_code', 'phone_pattern', 'icon', 'createAt', 'updatedAt')
    search_fields = ('title', 'phone_code')
    date_hierarchy = 'createAt'


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'createdAt', 'updatedAt')
    search_fields = ('title',)
    list_filter = ('country',)
    date_hierarchy = 'createdAt'