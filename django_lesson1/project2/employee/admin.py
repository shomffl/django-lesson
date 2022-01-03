from django.contrib import admin
from .models import Employee, Department, Club

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Club)
