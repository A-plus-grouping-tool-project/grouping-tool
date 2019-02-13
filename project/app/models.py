from django.db import models
from django.contrib.postgres.fields import ArrayField

SEP = ', '

class Course(models.Model):
    course_name = models.CharField(max_length=20)
    course_id = models.IntegerField(default=0)
    
    def __str__(self):
        return self.course_name

class Student(models.Model):
    username = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)
    #def __str__(self):
    #    return self.id + SEP + self.username + SEP + self.student_id +  SEP + self.email

class Group(models.Model):
    group_id = models.IntegerField(default=0)
    course_id = models.IntegerField()
    students = models.ManyToManyField(Student)

    #def __str__(self):
    #    return self.group_id + SEP + self.course_code
