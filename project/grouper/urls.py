from django.urls import path

from . import views

urlpatterns = [
    path('', views.group_students, name='group_students'),
]
