from .models import Comment
from django import forms
from django.utils.text import slugify


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
