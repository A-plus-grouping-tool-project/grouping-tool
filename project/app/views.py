from django.http import HttpResponse
from project.credentials import API_TOKEN
import requests
from django.shortcuts import render

def mainPage(request):
    return HttpResponse("Hello, world. You're at the app main page.")

def query(request):
    contents = requests.get('http://localhost:8000/api/v2/users/2',
                            headers={'Authorization': f'Token {API_TOKEN}'})
    return HttpResponse(contents);

def teacherView(request):
    context = {}
    return render(request, 'pages/teacherView.html',context)
