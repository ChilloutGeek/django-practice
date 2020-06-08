from django.shortcuts import render,redirect,reverse

from django.views.generic import ListView,DetailView,TemplateView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


from .forms import CreateUserForm, ProfileForm
from .models import Account 

# Create your views here

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        
        form = CreateUserForm(request.POST)
         
        if form.is_valid():
            user = form.save()
            profile = Account.objects.create(user=user)
            messages.success(request, 'you have succesfully registered')
            return redirect ('login')
    
    return render(request, 'users/registercontent.html',{'form':form})

def loginpage(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog_home')

        else:
            return redirect('login')
            messages.error(request, 'username or password is incorrect')


    return render(request, 'users/loginpage.html')

def logoutuser(request):

    logout(request)
    return redirect('login')


class UserProfile(TemplateView):

    template_name = 'users/profilepage.html'

class ProfileEdit(TemplateView):

    template_name = 'users/editprofile.html'

    def get(self,request):
        profile = Account.objects.get(user=request.user)
        form = ProfileForm(instance=profile)

        return render(request, self.template_name, {'form':form})

    def post(self,request):
        profile = User.objects.filter(user=request.user)

        form = ProfileForm(request.POST,request.FILES, instance=profile)

        if form.is_valid():
            acc = form.save(commit=False)
            acc.user = request.user
            acc.save()
            return redirect('blog_home')
        return render(request, self.template_name, {'form':form})


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

