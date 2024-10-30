from django import forms

from task_tracker.models import Comment


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'content', 'photo', 'specs']
        widgets = {
            'content': forms.Textarea
        }