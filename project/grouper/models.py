from django.db import models

# Create your models here.
class Student(models.Model):
    group = models.IntegerField()
    id = models.IntegerField()
    username = models.CharField(max_length=50) 
    student_id = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
