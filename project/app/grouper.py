import json, requests
from apirequests import views
from app.models import Student, Group, Course
from app import courses, students
from . import csv_maker

def group_students(group_size = 3, course_id = 1):
    course = courses.add_course(course_id)
    group_id_iterator = 1
    group = init_group(course, group_id_iterator)
    students_on_course = Student.objects.filter(courses__course_id = course_id)
    groupless = [i for i in students_on_course if not i.group_set.filter(course__course_id = course_id).exists()]
    print(len(groupless))
    if len(groupless) > 0:
        group.save()
    for i in range(len(groupless)):
        group.students.add(groupless[i])
        group.save()
        if (i+1) % group_size == 0 and i+1 != len(groupless):
            group_id_iterator += 1
            group = init_group(course, group_id_iterator)
            group.save()

def init_group(course, group_id):
    group = Group()
    group.group_id = group_id
    group.course = course
    return group

def delete_group(identifier):
    Group.objects.get(id=identifier).delete()

def find_empty_group(course_id):
    Group.objects.filter(course = course_id).filter(students = None)

def truncate():
    Course.objects.all().delete()
    Group.objects.all().delete()
    Student.objects.all().delete()
