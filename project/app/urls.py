from django.urls import path

from . import views
from apirequests import views as apiviews
from grouper import views as groupviews

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('query/', views.query, name='query'),
    path('students_from_course/', apiviews.students_from_course, name='students_from_course'),
    path('group_students/', groupviews.group_students, name='group_students')
]
