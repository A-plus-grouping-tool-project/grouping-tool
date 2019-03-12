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
    student_id = models.IntegerField(default=-1)
    student_no = models.CharField(max_length=10, default='000000')
    email = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)
    def __str__(self):
        return f'%s{SEP} %s{SEP} %s{SEP} %s' % \
            (self.student_id, self.username, self.student_no, self.email)

class Group(models.Model):
    group_id = models.IntegerField(default=0)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )
    students = models.ManyToManyField(Student)

    def __str__(self):
        return f'%s{SEP} %s' % \
            (self.group_id, self.course)
