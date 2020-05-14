from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.shortcuts import render,redirect,reverse



from .forms import CreateUserForm

# Create your views here.ssss
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        
        form = CreateUserForm(request.POST)
         
        if form.is_valid():
            form.save()
            user = c
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
            messages.error(request, 'userame or password is incorrect')


    return render(request, 'users/loginpage.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

