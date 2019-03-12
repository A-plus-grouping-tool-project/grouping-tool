import json, requests
from apirequests import views
from app.models import Course

def add_course(id, cname = "noname"):
    # course_response_object = json.loads(views.get_course(course_id))
    if course_in_database(id) == False:
        course = Course()
        course.course_id = id
        course.course_name = cname
        course.save()
        return course
    else:
        return Course.objects.get(course_id = id)

def course_in_database(id):
    return Course.objects.filter(course_id = id).exists()

def resolve_course_id(request):
    cid = -1
    scid = request.session['course_id']
    cname = request.session['course_name']
    resp = views.get_courses()
    data = json.loads(resp.content)
    for i in data['results']:
        print(i['html_url'][7:], scid)
        if i['html_url'][7:] == scid:
            cid = i['id']
    if cid != -1:
        add_course(cid, cname)
    return cid