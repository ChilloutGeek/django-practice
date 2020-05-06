from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView

from .models import Post
from .forms  import BlogForm
from django.shortcuts import render,redirect
# Create your views here

class BlogPost(ListView):

    model = Post
    template_name = 'blog/content.html'
    context_object_name = "blog_entry"

class BlogView(DetailView):
    model = Post
    template_name = 'blog/detailview.html'

class BlogCreate(TemplateView):

    template_name = "blog/createblog.html"

    def get(self,request): #get modelform
        form = BlogForm()
        return render(request,self.template_name,{'form':form})


    def post(self, request): #post method modelform

        form = BlogForm(request.POST)
        
        if form.is_valid(): 
            post = form.save(commit=False) #get modelform data but do not save to database
            post.author = request.user #get user data from author model
            post.save() #save to database
            return redirect ('/home')
        return render(request,self.template_name,{'form':form,})


def home(request):
    return render(request, 'blog/dashboard.html')

def about(request):
    return render(request, 'blog/about_me.html')
