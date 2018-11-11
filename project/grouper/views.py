from django.shortcuts import render
from django.http import HttpResponse
import json
from apirequests import views

def group_students(request):
    #define group size
    size = 3
    #HttpResponse from apirequests app's studentsFromCourse function
    #Currently parameter doesn't affect return value.
    resp = views.students_from_course(1)
    #using Python's json library to extract the content
    data = json.loads(resp.content)
    #some assisting variables
    groups = []
    group = []
    j = 0
    groups_as_text = ''
    #grouping logic
    for i in range(data['count']):
        student_object = data['results'][i]
        if j < size:
            group.append(student_object)
            j += 1
        else:
            groups.append(group)
            group = [student_object]
            j = 1
    if (len(group) != 0):
        groups.append(group)
    #builds a string representation of the data
    for i in range(len(groups)):
        if i == 0:
            groups_as_text += ('group '+ str(i+1) +':')
        else:
            groups_as_text += ('\ngroup '+ str(i+1) +':')
        for j in groups[i]:
            groups_as_text += '\n' +str(j)
    return HttpResponse(groups_as_text, content_type='text/plain')
