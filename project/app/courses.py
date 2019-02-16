import json
from apirequests import views
from app.models import Course

def add_course(id):
    # course_response_object = json.loads(views.get_course(course_id))
    if course_in_database(id) == False:
        course = Course()
        course.course_id = id
        course.save()
        return course
    else:
        return Course.objects.get(course_id = id)

def course_in_database(id):
    return Course.objects.filter(course_id = id).exists()
