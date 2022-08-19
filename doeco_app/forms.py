from .models import FreeComment, FreePost
from django import forms

class FreePostForm(forms.ModelForm):
    class Meta:
        model = FreePost
        fields = ['title', 'body', 'photo']

class FreeCommentForm(forms.ModelForm):
    class Meta:
        model = FreeComment
        fields = ['comment']