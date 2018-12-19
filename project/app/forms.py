from django import forms
from .models import Group

#Edit group dialog form
class EditGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('students',)
