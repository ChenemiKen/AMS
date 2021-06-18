from os import name
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    other_names = models.CharField(max_length= 50)
    mat_no = models.CharField(max_length=10)
    email = models.EmailField()
    department = models.CharField(max_length=20)
    level = models.IntegerField()
    fingerprintId = models.IntegerField()


class Register(models.Model):
    name = models.CharField(max_length=10)
    reg_id = models.CharField(max_length=10)
    password = models.CharField(max_length=250)


class Session(models.Model):
    title = models.CharField(max_length=15)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    register = models.ForeignKey(to=Register, on_delete=CASCADE)