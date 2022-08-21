from django.contrib import admin

from standard.models import standard, subject

# Register your models here.


@admin.register(standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ['schoolId', 'classId', 'email',
                    'name', 'password']


@admin.register(subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subjectId', 'subjectName']
