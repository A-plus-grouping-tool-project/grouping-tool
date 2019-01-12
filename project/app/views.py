from django.http import HttpResponse
from project.credentials import API_TOKEN
import requests
from django.shortcuts import render
from app.models import Group
from app.models import Student
from .forms import EditGroupForm
from django.views.generic import ListView, UpdateView
from django.template.loader import render_to_string


def mainPage(request):
    return HttpResponse("Hello, world. You're at the app main page.")

def query(request):
    contents = requests.get('http://localhost:8000/api/v2/users/2',
                            headers={'Authorization': f('Token {API_TOKEN}')})
    return HttpResponse(contents);

class teacherView(ListView):
    model = Group
    template_name = 'pages/teacherView.html'

    def get_queryset(self):
        return Group.objects.all()

class edit_group(UpdateView):
    model = Group
    form_class = EditGroupForm
    template_name = 'pages/modals/editGroupDialog.html'

    #add students without a group to modals data
    def get_context_data(self, **kwargs):
        context = super(edit_group, self).get_context_data(**kwargs)
        context['studentsWithoutGroup'] = Student.objects.all()
        return context

    #Add group_id to the request
    def dispatch(self, *args, **kwargs):
        self.id = kwargs['pk']
        return super(edit_group, self).dispatch(*args, **kwargs)

    #Do if form is valid
    def form_valid(self, form):
        form.save()
        item = Group.objects.get(id=self.id)
        #Call the success dialog
        return HttpResponse(render_to_string('pages/modals/editGroupDialogSuccess.html', {'group': item}))
