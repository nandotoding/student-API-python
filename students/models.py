from django.db import models


class Student(models.Model):
    studentName = models.CharField(max_length=255)
    studentMajor = models.CharField(max_length=255)
    studentAge = models.IntegerField()
