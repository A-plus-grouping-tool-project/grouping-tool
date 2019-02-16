import json
from apirequests import views
from app.models import Course

def add_course(course_id):
    # course_response_object = json.loads(views.get_course(course_id))
    course = Course()
    course.course_id = course_id
    course.save()

def course_in_database(id):
    return Course.objects.filter(course_id = id).exists()