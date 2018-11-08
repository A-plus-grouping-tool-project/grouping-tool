from django.shortcuts import render
from django.http import HttpResponse
from project.credentials import API_TOKEN
import requests

API_URL = 'http://localhost:8000/api/v2'

#Returns all users from api
def get_users():
    users = requests.get('{API_URL}/users/',
                            headers={'Authorization': f'Token {API_TOKEN}'})
    return HttpResponse(users)

#Returns all courses from api
def get_courses():
    courses = requests.get('{API_URL}/courses/',
                            headers={'Authorization': f'Token {API_TOKEN}'})
    return HttpResponse(courses)

#Returns user via their a-plus user ID
def find_user(user_id):
    user = requests.get(f'{API_URL}/users/{user_id}',
                        headers={'Authorization': f'Token {API_TOKEN}'})
    if user.status_code == 200:
        return HttpResponse(user)
    else:
        return HttpResponse(f'Something went wrong finding user. Is the user_id: {user_id} correct?')

#Returns all the students from course course id hard coded for testing purposes
def students_from_course(course_id):
    course_id = 1
    students = requests.get(f'{API_URL}/courses/{course_id}/students/',
                            headers={'Authorization': f'Token {API_TOKEN}'})
    if students.status_code == 200:
        return HttpResponse(students)
    else:
        return HttpResponse(f'Something went with your request. Is the course_id: {course_id} correct?')