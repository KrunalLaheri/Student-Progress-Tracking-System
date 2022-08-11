from django.contrib import admin

from standard.models import standard, subject

# Register your models here.


@admin.register(standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ['school_id', 'id',
                    'name', 'password']


@admin.register(subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_id', 'subject_name']
