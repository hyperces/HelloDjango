from django.contrib import admin
from .models import *

# Register your models here.



class BoardAdmin(admin.ModelAdmin):
    search_fields = ['title']


class EmployeesAdmin(admin.ModelAdmin):
    search_fields = ['FIRST_NAME', 'LAST_NAME', 'MANAGER_ID']
    list_display = ['FIRST_NAME', 'LAST_NAME', 'MANAGER_ID']
    list_filter = ['HIRE_DATE', 'JOB_ID', 'DEPARTMENT_ID','MANAGER_ID']

admin.site.register(Board, BoardAdmin)
admin.site.register(Employees, EmployeesAdmin)