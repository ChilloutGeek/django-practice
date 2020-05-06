from django.urls import path
from . import views
from .views import BlogPost, BlogView,BlogCreate
urlpatterns = [
    path('home/', BlogPost.as_view(), name = 'blog-home'),
    path('about_me/',views.about),
    path('home/entry/<int:pk>/', BlogView.as_view(), name = 'blog-view'),
    path('home/createblog/', BlogCreate.as_view(), name = 'blog-create')
]