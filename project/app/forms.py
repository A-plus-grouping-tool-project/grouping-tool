from django import forms
from .models import Group

class EditGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'maxsize', 'course_code', 'type', 'students',)