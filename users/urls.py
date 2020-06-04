from django.urls import path
from . import views
from .views import UserProfile,ProfileEdit
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name= 'register'),
    path('login/', views.loginpage, name= 'login'),
    path('logout/', views.logoutuser, name= 'logout'),
    path('home/profile', UserProfile.as_view(), name = 'profile'),
    path('home/profile/changepassword/', auth_views.PasswordChangeView.as_view(template_name='users/passwordchange.html'), name= 'changepassword'),
    path('home/profile/changepassworddone/', auth_views.PasswordChangeDoneView.as_view(template_name='users/passwordchangedone.html'), name= 'password_change_done'),
    path('home/profile/editprofile/', ProfileEdit.as_view(), name='editprofile'),
]