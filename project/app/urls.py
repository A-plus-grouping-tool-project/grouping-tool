from django.urls import path

from . import views
from apirequests import views as apiviews

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('query/', views.query, name='query'),
    path('students_from_course/', apiviews.students_from_course, name='students_from_course')
]