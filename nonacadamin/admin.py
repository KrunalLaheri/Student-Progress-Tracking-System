
from django.contrib import admin

from nonacadamin.models import categori, level, participation, subcategory

# Register your models here.


@admin.register(categori)
class Admin(admin.ModelAdmin):
    list_display = ['catId', 'catName']


@admin.register(subcategory)
class Admin(admin.ModelAdmin):
    list_display = ['subCatId', 'catId', 'subCatName']


@admin.register(level)
class Admin(admin.ModelAdmin):
    list_display = ['lvlId', 'lvlName']


@admin.register(participation)
class Admin(admin.ModelAdmin):
    list_display = ['coCurricularId', 'category',
                    'subCategory', 'studentId', 'studentName', 'year', 'date']
