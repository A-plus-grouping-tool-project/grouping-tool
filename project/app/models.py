from django.db import models
from django.contrib.postgres.fields import ArrayField

SEP = ', '

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50) 
    student_id = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.id + SEP + self.username + SEP + self.student_id +  SEP + self.email

class Group(models.Model):
    group_id = models.IntegerField()
    course_code = models.CharField(max_length=10)
    students = models.ManyToManyField(Student)
    group_type = models.IntegerField()

    def __str__(self):
        return self.group_id + SEP + self.course_code + SEP + self.group_type


class Type(models.Model):
    type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    max_size = models.IntegerField()
    