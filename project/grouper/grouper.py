import json
from apirequests import views
from app.models import Student, Group, Students_in_course
from . import csv_maker

#def group_students(request):
#    #define group size
#    size = 3
#    #HttpResponse from apirequests app's studentsFromCourse function
#    #Currently parameter doesn't affect return value.
#    resp = views.students_from_course(1)
#    #using Python's json library to extract the content
#    data = json.loads(resp.content)
#    #some assisting variables
#    j = 0
#    group_id = 1
#    #grouping logic
#    for i in range(data['count']):
#        if(i == 0):
#            csv_maker.create_csv()
#        else:
#            student_object = data['results'][i]
#            student_object.update({'group_id':group_id}) #student is linked to group with group-key
#            csv_maker.export_to_csv(student_object)
#            if j < size:
#                j += 1
#            else:
#                group_id += 1
#                j = 1
#    return HttpResponse('check your project-folder for groups.csv')

#wip
def group_students(group_size =  3, course_id = 1):
    resp = views.students_from_course(course_id)
    data = json.loads(resp.content)
<<<<<<< HEAD
    course_students = map(format_student_data, data['count'])
    print(course_students)
     
#wip
def format_student_data(student_object):
=======
    for i in range(data['count']):
        student = data['results'][i]
        student_to_database(student, course_id)
        group.group_id = group_id_iterator
        group.students.add(student['id'])
        if i % group_size == 0:
            group.save()
            group = Group()
            group_id_iterator += 1
            group.course_id = group_id_iterator
    
def student_to_database(student_object, course_id):
>>>>>>> 40ad531... Add functionality to group_students
    student = Student()

    #student.id = student_object['group_id']
    student.id = student_object['id']
    student.username = student_object['username']
    student.email = student_object['email']
    if(student_object['student_id'] != None):
        student.student_id = student_object['student_id']
    student.save()
<<<<<<< HEAD
=======
    if (course_id != None):
        student_in_course = Students_in_course()
        student_in_course.student = student_object['id']
        student_in_course.course = course_id
    #return student()
>>>>>>> 40ad531... Add functionality to group_students
