from django.db import models
from tester_helper import pw_generator, ID_generator
from school.models import School


class subject(models.Model):
    subjectId = models.IntegerField()
    subjectName = models.CharField(
        max_length=20, db_index=True, unique=True, primary_key=True)

    def __str__(self):
        return self.subjectName


class standard(models.Model):
    schoolId = models.ForeignKey(School, on_delete=models.DO_NOTHING)
    classId = models.CharField(max_length=10,
                               blank=True, unique=True, primary_key=True, editable=False)
    className = models.CharField(max_length=20, db_index=True)
    teacherName = models.CharField(max_length=50)
    # subject = models.ManyToManyField(subject)
    password = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    profilePhoto = models.ImageField(null=True,
                                     upload_to=None, height_field=None, width_field=None, max_length=100)

    def save(self, *args, **kwargs):
        self.classId = ID_generator()
        self.password = pw_generator()
        super(standard, self).save(*args, **kwargs)

    def __str__(self):
        return self.classId


class Usertoken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()
