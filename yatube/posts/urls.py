# posts/urls.py
from django.urls import path

from . import views
from django.urls import path, include


app_name = 'posts'

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/', views.posts, name='posts_list'),
    path('group_posts/', views.group_posts, name='group_posts_list'),
]