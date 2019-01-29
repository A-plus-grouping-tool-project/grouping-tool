from django.http import HttpResponse
from project.credentials import API_TOKEN
import requests
from django.shortcuts import render
from app.models import Group
from app.models import Student
from .forms import EditGroupForm, ExperimentalForm, newGroupForm
from . import grouper, courses, students
from . import csv_maker
from django.views.generic import ListView, UpdateView, TemplateView
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .forms import newGroupForm

def mainPage(request):
    return HttpResponse("Hello, world. You're at the app main page.")

def query(request):
    contents = requests.get('http://localhost:8000/api/v2/users/2',
                            headers={'Authorization': f('Token {API_TOKEN}')})
    return HttpResponse(contents)

def group_students(request):
    cid = courses.resolve_course_id(request)
    if cid != -1:
        students.create_student_entries(cid)
        gs = request.session.get('group_size', 3)
        grouper.group_students(course_id = cid, group_size = gs)
    return HttpResponse('check your dadabase :D')


@method_decorator(staff_member_required, name='dispatch')
class teacherView(ListView):
    raise_exception = True
    model = Group
    template_name = 'pages/teacherView.html'

    def get(self, request):
        name = request.user.first_name
        return render(request, self.template_name, {'nimi': name})

    def get_queryset(self):
        return Group.objects.all().order_by('group_id')

class studentView(ListView):
    model = Group
    template_name = 'pages/studentView.html'

    def get_queryset(self):
        return Group.objects.all()

class view_group(UpdateView):
    model = Group
    form_class = EditGroupForm
    template_name = 'pages/modals/viewGroupDialog.html'

    #add students in the group to modals data
    def get_context_data(self, **kwargs):
        context = super(view_group, self).get_context_data(**kwargs)
        groupStudents = Group.objects.get(id=self.id).students.all()
        context['studentsInGroup'] = set(groupStudents)
        return context

    #Add group_id to the request
    def dispatch(self, *args, **kwargs):
        self.id = kwargs['pk']
        return super(view_group, self).dispatch(*args, **kwargs)

    #Do if form is valid
    def form_valid(self, form):
        form.save()
        item = Group.objects.get(id=self.id)
        #Call the success dialog
        return HttpResponse(render_to_string('pages/modals/editGroupDialogSuccess.html', {'group': item}))

class edit_group(UpdateView):
    model = Group
    form_class = EditGroupForm
    template_name = 'pages/modals/editGroupDialog.html'

    #add students without a group to modals data
    def get_context_data(self, **kwargs):
        context = super(edit_group, self).get_context_data(**kwargs)
        allStudents = Student.objects.all()
        allGroupIds = Group.objects.values('id')
        #get students which are in some group
        groupStudents = []
        for id in allGroupIds:
            help = Group.objects.get(id=id.get('id')).students.all()
            groupStudents.extend(help)
        #get students without a group
        context['studentsWithoutGroup'] = set(allStudents).difference(set(groupStudents))
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

class experimental(TemplateView):
    template_name = 'pages/experimental.html'

    def get(self, request):
        form = ExperimentalForm()
        if 'course_id' in request.session.keys():
            msg = "grouper pointing to course " +request.session['course_id']
        else:
            msg = "Grouper not pointing to any course. LTI-authenticate from aplus."
        return render(request, self.template_name, {'form': form, 'msg': msg})

    def post(self, request):
        form = ExperimentalForm(request.POST)
        if form.is_valid():
            group_size = form.cleaned_data['group_size']
            delete_rows = form.cleaned_data['delete_rows']
        args = {'form': form, 'group_size': group_size}
        if delete_rows:
            grouper.truncate()
        if group_size is not None:
            request.session['group_size'] = group_size
            group_students(request)
        return render(request, self.template_name, args)

class new_group(TemplateView):
    model = Group
    template_name = 'pages/modals/newGroupView.html'

    def get(self, request):
        form = newGroupForm
        allStudents = Student.objects.all()
        allGroupIds = Group.objects.values('id')
        #get students which are in some group
        groupStudents = []
        for id in allGroupIds:
            help = Group.objects.get(id=id.get('id')).students.all()
            groupStudents.extend(help)
        #get students without a group
        data = set(allStudents).difference(set(groupStudents))
        args = {'studentsWihtoutgroup': data, 'form': form}
        print(data)
        return render(request, self.template_name, args)
