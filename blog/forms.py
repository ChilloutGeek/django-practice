from django.forms import ModelForm
from django import forms
from .models import Post

class BlogForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body',]
class FormOnly(forms.Form):
    title = forms.CharField(label='title', max_length=100)