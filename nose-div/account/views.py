from django.shortcuts import render
from  .models import User, Post
from django.views.generic.list import ListView
# Create your views here.

class UserList(ListView):
    # specify the model for list view
    queryset = User.objects.all().order_by("name")
    template_name = "users/list.html"
    user_object_name = "users"

class  PostList(ListView):
    queryset = User.objects.all().order_by("publish_date")
    template_name = "post/list.html"
    user_object_name = "posts"