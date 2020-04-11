from django.contrib import admin

# Register your models here.
from scraping.models import Employee, Job

admin.site.register(Employee)
admin.site.register(Job)
