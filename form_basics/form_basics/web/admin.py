from django.contrib import admin
from form_basics.web.models import Employee

# admin.site.register(Employee)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'role')
