from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.group_students, name='group_students'),
]
