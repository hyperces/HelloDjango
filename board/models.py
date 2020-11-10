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