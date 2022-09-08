# posts/urls.py
from django.urls import path

from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.index),
    #path('posts/', views.group_list, name='group_list'),
    path('posts/', views.group_list, name='group_list'),
]