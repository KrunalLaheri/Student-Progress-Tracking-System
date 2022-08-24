from django.contrib import admin
from .models import exam, result
# Register your models here.


@admin.register(exam)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['schoolId', 'classId', 'examId', 'examName']


@admin.register(result)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['schoolId', 'classId',
                    'studentId', 'resultId', 'sem', 'year', 'data', 'studentName', 'avg']
