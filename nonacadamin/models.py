import uuid
from django.db import models
from school.models import School
from standard.models import standard
from student.models import student


class categori(models.Model):
    catId = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    catName = models.CharField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return self.catName


class subcategory(models.Model):
    subCatId = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    catName = models.ForeignKey(categori, on_delete=models.DO_NOTHING)
    subCatName = models.CharField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return self.subCatName


class level(models.Model):
    lvlId = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    lvlName = models.CharField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return self.lvlName


class participation(models.Model):
    category = models.ForeignKey(categori, on_delete=models.DO_NOTHING)
    classId = models.ForeignKey(standard, on_delete=models.DO_NOTHING)
    coCurricularId = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    date = models.DateField()
    isVerified = models.BooleanField(default=False)
    level = models.ForeignKey(level, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    points = models.IntegerField(blank=True, default=0)
    schoolId = models.ForeignKey(School, on_delete=models.DO_NOTHING)
    studentId = models.ForeignKey(student, on_delete=models.DO_NOTHING)
    studentName = models.CharField(max_length=100)
    subCategory = models.ForeignKey(subcategory, on_delete=models.DO_NOTHING)
    year = models.CharField(max_length=10)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.studentName
