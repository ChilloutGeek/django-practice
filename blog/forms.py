from django.forms import ModelForm
from django import forms
from .models import Post, Category, Comment

#category_list = [('sport', 'sport'),('games','games')]


category = Category.objects.all().values_list('name','name')
category_list = []

for item in category:
    category_list.append(item)

class BlogForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'body', 'category','photo']

        widgets = {
            'title':forms.TextInput(attrs={"class":'form-control'}),
            'body':forms.TextInput(attrs={"class":'form-control'}),
            'category':forms.Select(choices=category_list,attrs={"class":'form-control'}),

        }


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name']

        widgets = {
             'name':forms.TextInput(attrs={"class":'form-control'}),

        }

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['text']

class SearchForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ['title']

        widgets = {
            'title':forms.TextInput(attrs={"class":'form-control'}),

        }

     
