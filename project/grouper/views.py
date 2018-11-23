from django.shortcuts import render
from django.http import HttpResponse
import json
from apirequests import views
from . import csv_maker

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
