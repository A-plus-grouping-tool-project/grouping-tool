from django.http import HttpResponse
from project.credentials import API_TOKEN
import requests
from django.shortcuts import render
from .models import Group
from .forms import EditGroupForm
from django.views.generic import ListView, UpdateView

def mainPage(request):
    return HttpResponse("Hello, world. You're at the app main page.")

def query(request):
    contents = requests.get('http://localhost:8000/api/v2/users/2',
                            headers={'Authorization': f('Token {API_TOKEN}')})
    return HttpResponse(contents);

#def teacherView(request):
#    context = {}
#    return render(request, 'pages/teacherView.html',context)

class teacherView(ListView):
    model = Group
    template_name = 'pages/teacherView.html'

    def get_queryset(self):
        return Group.objects.all()

class edit_group(UpdateView):
    model = Group
    context_object_name = 'group'
    form_class = EditGroupForm
    template_name = 'dialog/editGroupDialog.html'

    def dispatch(self, *args, **kwargs):
        self.course_code = kwargs['pk']
        return super(edit_group, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        group = Group.objects.get(course_code=self.course_code)
        return HttpResponse(render_to_string('dialog/editGroupDialogSuccess.html', {'group' : group}))