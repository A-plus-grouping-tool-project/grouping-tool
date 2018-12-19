import json
from apirequests import views
from app,models import Student, Group, Type
from . import csv_maker
from . import models



def group_students(request):
    #define group size
    size = 3
    #HttpResponse from apirequests app's studentsFromCourse function
    #Currently parameter doesn't affect return value.
    resp = views.students_from_course(1)
    #using Python's json library to extract the content
    data = json.loads(resp.content)
    #some assisting variables
    j = 0
    group_id = 1
    #grouping logic
    for i in range(data['count']):
        if(i == 0):
            csv_maker.create_csv()
        else:
            student_object = data['results'][i]
            student_object.update({'group_id':group_id}) #student is linked to group with group-key
            csv_maker.export_to_csv(student_object)
            if j < size:
                j += 1
            else:
                group_id += 1
                j = 1
    return HttpResponse('check your project-folder for groups.csv')

#wip
def group_students(group_size =  3, course_id = 1):
    resp = views.students_from_course(course_id)
    data = json.loads(resp.content)
    course_students = map(format_student_data, data['count'])
    print(course_students)
     
#wip
def format_student_data(student_object):
    student = Student()

    #student.id = student_object['group_id']
    student.id = student_object['id']
    student.username = student_object['username']
    student.student_id = student_object['student_id']
    student.email = student_object['email']
    student.save()
