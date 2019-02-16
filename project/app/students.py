import json
from apirequests import views
from . import courses
from app.models import Student, Course

def add_student(student_object, cid = -1):
    # student_response_object = json.loads(views.get_student(student_id))
    if student_in_database(student_object['id']) == False:
        student = Student()
        student.id = student_object['id']
        student.username = student_object['username']
        student.email = student_object['email']
        if student_object['student_id'] == None:
            student.student_id = '000000'
        else:
            student.student_id = student_object['student_id']
        student.save()
        if cid != -1:
            student.courses.add(Course.objects.get(course_id = cid))
        student.save()
        return student

def student_in_database(id):
    return Student.objects.filter(id = id).exists()
