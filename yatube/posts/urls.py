# posts/urls.py
from django.urls import path

from . import views
from django.urls import path, include


app_name = 'posts'

urlpatterns = [
    path('', views.index, name="index"),
    #path('posts/', views.posts, name='posts_list'),
    path('group_list/', views.group_list, name='group_list'),
]