import json
from apirequests import views
from app.models import Student, Group, Course
from app import courses, students
from . import csv_maker

#wip
def group_students(group_size =  3, course_id = 1):
    resp = views.students_from_course(course_id)
    data = json.loads(resp.content)
    course = courses.add_course(course_id)
    group_id_iterator = 1
    group = init_group(course_id, group_id_iterator)
    group.save()
    for i in range(data['count']):
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
