from django.urls import path
from . import views
from .views import BlogPost,BlogView,BlogCreate,BlogUpdate,BlogDelete,AboutMe,BlogAddCategory
urlpatterns = [

    path('home/', BlogPost.as_view(), name = 'blog-home'),
    path('about_me/',AboutMe.as_view(), name= 'blog-about'),
    path('home/entry/<int:pk>/', BlogView.as_view(), name = 'blog-view'),
    path('home/createblog/', BlogCreate.as_view(), name = 'blog-create'),
    path('home/updateblog/<int:pk>/', BlogUpdate.as_view(), name = 'blog-update'),
    path('home/blogdelete/<int:pk>/', BlogDelete.as_view(), name = 'blog-delete'),
    path('home/createcategory/', BlogAddCategory.as_view(), name = 'blog-category'),
    path('home/blogcategory/<str:category>/', views.CategoryPage, name = 'blog-categorypage'),
]   