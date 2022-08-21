from django.contrib import admin
from .models import exam, result
# Register your models here.


@admin.register(exam)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['schoolId', 'standardId', 'examId', 'examName']


@admin.register(result)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['schoolId', 'standardId',
                    'studentId', 'resultId', 'examName', 'data', 'year']
