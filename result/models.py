import uuid
from django.db import models
from school.models import School
from student.models import student
from standard.models import standard

# Create your models here.


class exam(models.Model):
    schoolId = models.ForeignKey(School, on_delete=models.DO_NOTHING)
    classId = models.ForeignKey(standard, on_delete=models.DO_NOTHING)
    examId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    examName = models.CharField(max_length=20)

    class Meta:
        unique_together = ('classId', 'examName')

    def __str__(self):
        return self.examName


class result(models.Model):
    schoolId = models.ForeignKey(School, on_delete=models.DO_NOTHING)
    classId = models.ForeignKey(standard, on_delete=models.DO_NOTHING)
    studentId = models.ForeignKey(student, on_delete=models.DO_NOTHING)
    resultId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    sem = models.ForeignKey(exam, on_delete=models.DO_NOTHING)
    # sem = models.CharField(max_length=20)
    # sem = models.ForeignKey(exam, on_delete=models.DO_NOTHING)
    year = models.CharField(max_length=20)
    data = models.JSONField()
    studentName = models.CharField(max_length=100)
    avg = models.FloatField()

    def __str__(self):
        return str(self.sem)
