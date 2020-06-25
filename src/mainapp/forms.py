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
        widgets = {
            'post_name' : forms.TextInput(attrs={'class':"form-control",}),
            'post_subject' : forms.TextInput(attrs={'class':"form-control",}),
            'post_content' : forms.Textarea(attrs={'class':"form-control", "rows":5}),
        }