from django.shortcuts import render,redirect,reverse

from django.views.generic import ListView,DetailView,TemplateView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


from .forms import CreateUserForm
from .models import Account 
# Create your views here.ssss
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        
        form = CreateUserForm(request.POST)
         
        if form.is_valid():
            form.save()
            messages.success(request, 'you have succesfully registered')
            return redirect ('login')
    
    return render(request, 'users/registercontent.html',{'form':form})

def loginpage(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog_home')

        else:
            messages.error(request, 'username or password is incorrect')


    return render(request, 'users/loginpage.html')

def logoutuser(request):

    logout(request)
    return redirect('login')


class UserProfile(TemplateView):

    template_name = 'users/profilepage.html'



class PasswordChangeView():
    
    template_name = 'users/passwordchange.html'


    def get(self, request):
        form = PasswordChangeForm()

        return render(request, self.template_name, {'form':form})

    def post(self,request):

        form = PasswordChangeForm(request.POST)

        if form.is_valid():
            
            form.save()

            return render(request,self.template_name, {'form':form})


class PasswordChangeDoneView():
    template_name = 'users/passwordchangedone.html'

