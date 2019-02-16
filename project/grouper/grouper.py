import json
from apirequests import views
from app.models import Student, Group, Course
from . import csv_maker

#wip
def group_students(group_size =  3, course_id = 1):
    resp = views.students_from_course(course_id)
    data = json.loads(resp.content)
    group_id_iterator = 1
    group = init_group(course_id, group_id_iterator)
    for i in range(data['count']):
        student = data['results'][i]
        student_object = student_to_database(student, course_id)
        group.students.add(student_object)
        if i % group_size == 0:
            group.save()
            group_id_iterator += 1
            group = init_group(course_id, group_id_iterator)

def init_group(course_id, group_id):
    group = Group()
    group.group_id = group_id
    group.course_id = course_id
    return group
    
def student_to_database(student_object, course_id = -1):
    student = Student()

    student.student_id = student_object['id']
    student.username = student_object['username']
    student.email = student_object['email']
    if(student_object['student_id'] != None):
        student.student_id = student_object['student_id']
    student.save()
    if (course_id != -1):
        course = Course()
        course.student = student_object['id']
        course.id = course_id
        course.save()
        student.courses.add(course)
    return student
