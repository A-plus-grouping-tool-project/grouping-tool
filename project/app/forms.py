from django import forms
from .models import Group

#Edit group dialog form
class EditGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('students',)

class ExperimentalForm(forms.Form):
    group_size = forms.IntegerField(required=False)
    delete_rows = forms.BooleanField(required=False)

class newGroupForm(forms.ModelForm):
    group_name = forms.CharField(label="Group name", max_length=100)

    class Meta:
        model = Group
        fields = ('name',)
