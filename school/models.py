from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class School(AbstractUser):
    school_name = models.CharField(
        max_length=100, blank=True, null=True, unique=True)
    school_code = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_no = models.CharField(max_length=10)
    address = models.TextField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'school_code']

    def __str__(self):
        return "{}".format(self.email)


class Usertoken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()
