import json
from apirequests import views
from app.models import Student, Group, Course
from app import courses, students
from . import csv_maker

def group_students(group_size =  3, course_id = 1):
    resp = views.students_from_course(course_id)
    data = json.loads(resp.content)
    course = courses.add_course(course_id)
    group_id_iterator = 1
    group = init_group(course_id, group_id_iterator)
    group.save()
    for i in range(data['count']):
        group.save()
        student = data['results'][i]
        student_object = students.add_student(student, course_id)
        group.students.add(student_object)
        group.save()
        if (i+1) % group_size == 0:
            group_id_iterator += 1
            group = init_group(course_id, group_id_iterator)
            group.save()

def init_group(course_id, group_id):
    group = Group()
    group.group_id = group_id
    group.course_id = course_id
    return group

def delete_group(identifier):
    Group.objects.get(id=identifier).delete()

def find_empty_group(course_id):
    Group.objects.filter(course = course_id).filter(students = None)
    
def student_to_database(student_object, course_id = -1):

    student = Student()

    student.student_id = student_object['id']
    student.username = student_object['username']
    student.email = student_object['email']
    if student_object['student_id'] != None:
        student.student_id = student_object['student_id']
    student.save()
    if course_id != -1:
        course = Course()
        course.student = student_object['id']
        course.id = course_id
        course.save()
        student.courses.add(course)
    return student
