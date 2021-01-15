from django import forms
from django.forms import ModelForm
import re

from .models import Post


class PostForm(ModelForm):
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message:
            message = re.sub(r'[a-zA-Z]+', '', message)
        return message

    class Meta:
        model = Post
        fields = ['message', 'is_published', 'photo', 'tag_set']