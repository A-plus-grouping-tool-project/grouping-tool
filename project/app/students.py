import json
from apirequests import views
from . import courses
from app.models import Student, Course

def add_student(student_object, course):
    # student_response_object = json.loads(views.get_student(student_id))
    if student_in_database(student_object['id']) == False:
        student = Student()
        student.student_id = student_object['id']
        student.username = student_object['username']
        student.email = student_object['email']
        if student_object['student_id'] == None:
            student.student_no = '000000'
        else:
            student.student_no = student_object['student_id']
        student.save()
        try:
            student.courses.get(course_id = course.id)
        except:
            student.courses.add(course)
            student.save()
        return student
    else:
        student = Student.objects.get(student_id = student_object['id'])
        try:
            student.courses.get(course_id = course.course_id)
        #student exists already, but has started a new course
        except:
            student.courses.add(course)
            student.save()
        return student

def student_in_database(id):
    return Student.objects.filter(student_id = id).exists()

def create_student_entries(course_id = 1):
    resp = views.students_from_course(course_id)
    data = json.loads(resp.content)
    course = courses.add_course(course_id)
    for i in range(data['count']):
        student = data['results'][i]
        add_student(student, course)
