from django.contrib import admin
from .models import People, Companies

# Register your models here.
# class PeopleAdmin(admin.ModelAdmin):
#     list_display = []

class CompaniesAdmin(admin.ModelAdmin):
    list_display = ['index', 'company']

admin.site.register(People)
admin.site.register(Companies, CompaniesAdmin)
