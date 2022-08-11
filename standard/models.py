from django.db import models
from helper import pw_generator, ID_generator
from django.contrib.auth.models import AbstractUser


class subject(models.Model):
    subject_id = models.IntegerField()
    subject_name = models.CharField(
        max_length=20, db_index=True, unique=True, primary_key=True)

    def __str__(self):
        return self.subject_name


class standard(models.Model):
    school_id = models.CharField(
        max_length=100, blank=True, null=True)
    id = models.CharField(max_length=10,
                          blank=True, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=20, db_index=True)
    subject = models.ManyToManyField(subject)
    password = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField()

    def save(self, *args, **kwargs):
        self.id = ID_generator()
        self.password = pw_generator()
        super(standard, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Usertoken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()
