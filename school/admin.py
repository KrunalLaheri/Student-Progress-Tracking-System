from django.contrib import admin
from .models import School

admin.site.register(School)

# @admin.register(School)
# class SchoolAdmin(admin.ModelAdmin):
#     list_display=['']
