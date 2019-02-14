from django.conf.urls import url

from . import views
from apirequests import views as apiviews
from grouper import views as groupviews
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.mainPage, name='mainPage'),
    url(r'^query/', views.query, name='query'),
    url(r'^students_from_course/', apiviews.students_from_course, name='students_from_course'),
    url(r'^group_students/', groupviews.group_students, name='group_students'),
    url(r'^teacher/', views.teacherView.as_view(), name='teacherView'),
    url(r'^student/', views.studentView.as_view(), name='studentView'),
    url(r'^edit_group/<pk>', views.edit_group.as_view(), name='edit_group'),
    url(r'^view_group/<pk>', views.view_group.as_view(), name='view_group'),
    url(r'^logout/', auth_views.LogoutView.as_view()),
]
