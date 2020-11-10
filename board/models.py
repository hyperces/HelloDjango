from django.db import models

# Create your models here.
from django.utils import timezone


class Board(models.Model):
    # id = models.IntegerField() 자동생성이므로 생략가능
    title = models.CharField(max_length=100)
    userid = models.CharField(max_length=20)
    regdate = models.DateTimeField(default=timezone.localtime)
    views = models.IntegerField(default=0)
    thumbup = models.IntegerField(default=0)
    contents = models.TextField()


class Employees(models.Model):
    # id = models.IntegerField() 자동생성이므로 생략가능
    EMPLOYEE_ID = models.CharField(max_length=100)
    FIRST_NAME = models.CharField(max_length=100)
    LAST_NAME = models.CharField(max_length=100)
    EMAIL = models.CharField(max_length=100)
    PHONE_NUMBER = models.CharField(max_length=100)
    HIRE_DATE = models.DateTimeField()
    JOB_ID = models.CharField(max_length=100)
    SALARY = models.IntegerField()
    COMMISSION_PCT = models.FloatField()
    MANAGER_ID = models.CharField(max_length=20)
    DEPARTMENT_ID = models.CharField(max_length=20)
