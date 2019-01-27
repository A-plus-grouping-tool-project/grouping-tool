from django.shortcuts import render
from django.http import HttpResponse
import json
from apirequests import views
from . import grouper
from . import csv_maker

def group_students(request):
    grouper.group_students()
    return HttpResponse('check your dadabase :D')
