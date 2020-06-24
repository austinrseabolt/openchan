from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_name',
            'post_subject',
            'post_content',
        ]
        labels = {
            'post_name':'Name',
            'post_subject':'Subject',
            'post_content':'Content',
        }