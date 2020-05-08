from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView

from .models import Post, Category, Comment
from .forms  import BlogForm, CategoryForm, CommentForm
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
            post = form.save(commit=False)
            post.author = request.user #get user from author model
            post.save()
            return redirect ('blog-home')

        if form.is_valid(): 
            post = form.save(commit=False) #get modelform data but do not save to database
            post.author = request.user #get user data from author model
            post.save() #save to database
            return redirect ('/home')

        return render(request,self.template_name,{'form':form,})

class BlogUpdate(TemplateView):

    template_name= "blog/blogupdate.html"



    def get(self,request,pk):
        postx = Post.objects.get(id=pk)

        form = BlogForm(instance=postx)
        return render(request,self.template_name,{'form':form})


    def post(self, request, pk):

        postx = Post.objects.get(id=pk) #object for update

        form = BlogForm(request.POST, instance=postx)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user #get user from author model
            post.save()
            return redirect ('blog-home')
        return render(request,self.template_name,{'form':form,})

class BlogDelete(TemplateView):

    template_name="blog/blogdelete.html"

    def get(self,request,pk):
        postxx = Post.objects.get(id=pk) #object for delete

        form = BlogForm(instance=postxx)

        return render(request,self.template_name,{'form':form})

    def post(self,request,pk):

        postxx = Post.objects.get(id=pk) #object for update
        form = BlogForm(request.POST, instance=postxx)
        
        if form.is_valid():
            
            postxx.delete()
            return redirect ('blog-home')

        return render(request,self.template_name,)

class BlogAddCategory(TemplateView):

    template_name="blog/addcategory.html"
 
    def get(self,request):
        
        form = CategoryForm()
        
        
        return render(request,self.template_name,{'form':form})


    def post(self, request):

        form = CategoryForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            return redirect ('blog-home')
        
        return render(request,self.template_name,{'form':form,})

def CommentsPage(request):

    form = CommentForm()
    commentxx = Comment.objects.all()
    
    if request.method=="POST":
        form = CommentForm(request.POST)
        
        
        if form.is_valid():
            
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('blog-home')
    
    return render(request, 'blog/blogcomments.html', {'form':form, 'commentxx':commentxx})

def CategoryPage(request, category):
    
    categorypost = Post.objects.filter(category=category)

    return render(request, 'blog/blogcategory.html', {'categorypost':categorypost})


class AboutMe(TemplateView):

    template_name ="blog/about_me.html"


