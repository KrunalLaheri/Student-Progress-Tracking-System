from django.db import models
from tester_helper import pw_generator, ID_generator
from standard.models import standard
from school.models import School


class student(models.Model):
    GENDER_CHOICES = [("Male", "Male"), ("Female", "Female")]
    schoolId = models.ForeignKey(School, on_delete=models.DO_NOTHING)
    classId = models.ForeignKey(standard, on_delete=models.DO_NOTHING)
    studentId = models.CharField(max_length=10,
                                 blank=True, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=20, db_index=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    address = models.TextField(max_length=250)
    admissionDate = models.DateField()
    password = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        self.studentId = ID_generator()
        self.password = pw_generator()
        super(student, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Usertoken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()
