from django import forms

from task_tracker.models import Task


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'description': forms.TextInput
        }