from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView

from .models import Post, Category, Comment
from .forms  import BlogForm, CategoryForm, CommentForm, SearchForm
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here

class BlogPost(ListView):
    login_required = True
    login_url = 'login'

    model = Post
    template_name = 'blog/content.html'
    context_object_name = "blog_entry"


class BlogView(TemplateView):
    login_required = True
    login_url = 'login'
    model = Post
    template_name = 'blog/detailview.html'
    
    def get(self,request,pk):
        form = CommentForm()
        post = Post.objects.get(pk=pk)
        comments = post.comment_set.all()
        return render(request,self.template_name,{'form':form,'post':post,'comments':comments})
    
    def post(self,request,pk):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST,request.FILES)
        comments = post.comment_set.all()
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return render(request,self.template_name,{'form':form,'post':post,'comments':comments, 'new_comment':new_comment})
            return redirect ('blog_home')

class BlogCreate(TemplateView):
    login_url = 'login'
    login_required = True
    template_name = "blog/createblog.html"

    def get(self,request): #get modelform
        form = BlogForm()
        return render(request,self.template_name,{'form':form})


    def post(self, request): #post method modelform

        form = BlogForm(request.POST, request.FILES)
        

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user #get user from author model
            post.save()
            return redirect ('blog_home')

        return render(request,self.template_name,{'form':form,})

class BlogUpdate(TemplateView):
    login_url = 'login'
    login_required = True
    template_name= "blog/blogupdate.html"



    def get(self,request,pk):
        postx = Post.objects.get(id=pk)

        form = BlogForm(instance=postx)
        return render(request,self.template_name,{'form':form})


    def post(self, request, pk):

        postx = Post.objects.get(id=pk) #object for update

        form = BlogForm(request.POST,request.FILES, instance=postx)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user #get user from author model
            post.save()
            return redirect ('blog_home')
        return render(request,self.template_name,{'form':form,})

class BlogDelete(TemplateView):
    login_required = True 
    login_url = 'login'  
    template_name="blog/blogdelete.html"

    def get(self,request,pk):
        postxx = Post.objects.get(id=pk) #object for delete

        form = BlogForm(instance=postxx)

        return render(request,self.template_name,{'form':form})

    def post(self,request,pk):

        postxx = Post.objects.get(id=pk) #object for update
        form = BlogForm(request.POST,request.FILES, instance=postxx)
        
        if form.is_valid():
            
            postxx.delete()
            return redirect ('blog_home')

        return render(request,self.template_name,)

class BlogAddCategory(TemplateView):

    login_required = True
    login_url = 'login'
    template_name="blog/addcategory.html"
 
    def get(self,request):
        
        form = CategoryForm()
        
        
        return render(request,self.template_name,{'form':form})


    def post(self, request):

        form = CategoryForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            return redirect ('blog_home')
        
        return render(request,self.template_name,{'form':form})

class BlogSearch(TemplateView):
   
   model = Post
   template_name = 'blog/blogsearch.html'
   
   def get(self,request):

    search_text = request.GET['search_text']

    posts = Post.objects.filter(title__icontains=search_text)

    return render(request, self.template_name, {'search_text':search_text, 'posts':posts})



   def post(self, request):
    
    search_text = request.POST['search_text']

    posts = Post.objects.filter(title__icontains=search_text)

    return render(request, self.template_name, {'search_text':search_text, 'posts':posts})




def CommentsPage(request):
    form = CommentForm()
    commentxx = Comment.objects.all()
    
    if request.method=="POST":
        form = CommentForm(request.POST)
        
        
        if form.is_valid():
            
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('blog_home')
    
    return render(request, 'blog/blogcomments.html', {'form':form, 'commentxx':commentxx})

def CategoryPage(request, category):
    
    categorypost = Post.objects.filter(category=category)


    return render(request, 'blog/blogcategory.html', {'categorypost':categorypost})


class AboutMe(TemplateView):

    template_name ="blog/about_me.html"


