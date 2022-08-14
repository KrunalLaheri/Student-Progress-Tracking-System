from django.contrib import admin
from .models import student


@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['school_id', 'standard_id', 'id', 'email',
                    'name', 'result', 'password']
